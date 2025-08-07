from itertools import islice
from typing import Optional, Sized, Union, List


from capymoa.base import Batch
import torch
import numpy as np
import pandas as pd
from tqdm import tqdm
import time

from capymoa._utils import batched
from capymoa.base import (
    BatchClassifier,
    BatchRegressor,
    Classifier,
    MOAPredictionIntervalLearner,
    Regressor,
)
from capymoa.classifier import (
    ConceptDriftMethodClassifier,
)
from capymoa.evaluation import (
    ClassificationEvaluator,
    ClassificationWindowedEvaluator,
    RegressionEvaluator,
    RegressionWindowedEvaluator,
    PredictionIntervalEvaluator,
    PredictionIntervalWindowedEvaluator,
)
from capymoa.instance import LabeledInstance, RegressionInstance
from capymoa.evaluation._progress_bar import resolve_progress_bar
from capymoa.evaluation.results import PrequentialResults
from capymoa.stream import Stream

def start_time_measuring():
    start_wallclock_time = time.time()
    start_cpu_time = time.process_time()

    return start_wallclock_time, start_cpu_time


def stop_time_measuring(start_wallclock_time, start_cpu_time):
    # Stop measuring time
    end_wallclock_time = time.time()
    end_cpu_time = time.process_time()

    # Calculate and print the elapsed time and CPU times
    elapsed_wallclock_time = end_wallclock_time - start_wallclock_time
    elapsed_cpu_time = end_cpu_time - start_cpu_time

    return elapsed_wallclock_time, elapsed_cpu_time

def _get_expected_length(
    stream: Stream, max_instances: Optional[int] = None
) -> Optional[int]:
    """Get the expected length of the stream."""
    if isinstance(stream, Sized) and max_instances is not None:
        return min(len(stream), max_instances)
    elif isinstance(stream, Sized) and max_instances is None:
        return len(stream)
    elif max_instances is not None:
        return max_instances
    else:
        return None

def _setup_progress_bar(
    msg: str,
    progress_bar: Union[bool, tqdm],
    stream: Stream,
    learner,
    max_instances: Optional[int],
):
    expected_length = _get_expected_length(stream, max_instances)
    progress_bar = resolve_progress_bar(
        progress_bar,
        f"{msg} {type(learner).__name__!r} on {type(stream).__name__!r}",
    )
    if progress_bar is not None and expected_length is not None:
        progress_bar.set_total(expected_length)
    return progress_bar

def _get_target(
    instance: Union[LabeledInstance, RegressionInstance],
) -> Union[int, np.double]:
    """Get the target value from an instance."""
    if isinstance(instance, LabeledInstance):
        return instance.y_index
    elif isinstance(instance, RegressionInstance):
        return instance.y_value
    else:
        raise ValueError("Unknown instance type")

class ConceptDriftDetectorEvaluator:

    def __init__(self):
        self.reset()
        self.measurements = {name: [] for name in self.metrics_header()}

    def reset(self):
        self.weight_observed = 0.0
        self.number_detections = 0.0
        self.number_detections_occurred = 0.0
        self.has_false_alarm = False
        self.number_changes = 0.0
        self.number_warnings = 0.0
        self.delay = 0.0
        self.total_delay = 0.0
        self.total_delay_false_alarm = 0.0
        self.delay_false_alarm = 0.0
        self.is_warning_zone = False
        self.input_values = 0.0
        self.has_change_occurred = False

    def metrics_header(self):
        performance_names = ["detected changes", "detected warnings", "true changes",
                             "delay detection (average)", "delay true detection (average)", 
                             "MTFA (average)", "MDR", "true changes detected"]
        return performance_names
    
    def get_measurements(self):
        self.measurements["detected changes"] = self.number_detections
        self.measurements["detected warnings"] = self.number_warnings
        self.measurements["true changes"] = self.number_changes
        if self.number_changes > 0:
            self.measurements["delay detection (average)"] = self.total_delay / self.number_changes
        else:
            self.measurements["delay detection (average)"] = 0.0

        if self.number_detections_occurred > 0:
            self.measurements["delay true detection (average)"] = self.total_delay / self.number_detections
        else:
            self.measurements["delay true detection (average)"] = 0.0

        if self.number_detections > 0:
            self.measurements["MTFA (average)"] = self.delay_false_alarm / (self.number_detections - self.number_detections_occurred)
        else:
            self.measurements["MTFA (average)"] = 0.0

        if self.number_changes > 0:
            self.measurements["MDR"] =  (self.number_changes - self.number_detections_occurred) /  self.number_changes
        else:
            self.measurements["MDR"] = 0.0

        self.measurements["true changes detected"] = self.number_detections_occurred
        
        return self.measurements

    def metrics(self):
        return [self.measurements[key] for key in self.metrics_header()]
    
    def add_result(self, example, ground_truth, class_votes):
        example = example.java_instance
        inst = example.getData()  # assuming method like Java's getData()
        self.input_values = int(inst.classValue())
        inst_weight = inst.weight()

        # classVotes[0] -> is Change
        # classVotes[1] -> is in Warning Zone
        # classVotes[2] -> delay
        # classVotes[3] -> estimation

        # print(f"Ground Truth {ground_truth}")
        # print(f"Drift Detector {class_votes[0]}")
        # print(f"Delay Detector {self.total_delay}")

        if inst_weight > 0.0 and len(class_votes) == 4:
            self.delay += 1
            self.weight_observed += inst.weight()

            if class_votes[0] == 1.0:
                self.number_detections += inst.weight()
                if self.has_change_occurred:
                    self.total_delay += self.delay - class_votes[2]
                    self.number_detections_occurred += inst.weight()
                    self.has_change_occurred = False
                    self.has_false_alarm = False
                    self.total_delay_false_alarm += self.delay_false_alarm
                    self.delay_false_alarm = 0.0
                else:
                    self.has_false_alarm = True
                    self.total_delay_false_alarm += self.delay_false_alarm
                    self.delay_false_alarm = 0.0

            if self.has_false_alarm:
                self.delay_false_alarm += 1

            if self.has_change_occurred and class_votes[1] == 1.0:
                if not self.is_warning_zone:
                    self.number_warnings += inst.weight()
                    self.is_warning_zone = True
            else:
                self.is_warning_zone = False

            if ground_truth == 1:
                self.number_changes += inst.weight()
                self.delay = 0
                self.has_change_occurred = True

def prequential_cd_delay_evaluation(
    stream: Stream,
    learner: Union[Classifier, Regressor],
    max_instances: Optional[int] = None,
    window_size: int = 1000,
    store_predictions: bool = False,
    store_y: bool = False,
    optimise: bool = True,
    restart_stream: bool = True,
    progress_bar: Union[bool, tqdm] = False,
    batch_size: int = 1,
    cd_ground_truth: Optional[List[int]] = None,
    delay_length: int = 0,
) -> PrequentialResults:
    """Run and evaluate a learner on a stream using prequential evaluation.

    Calculates the metrics cumulatively (i.e. test-then-train) and in a
    window-fashion (i.e. windowed prequential evaluation). Returns both
    evaluators so that the user has access to metrics from both evaluators.

    :param stream: A data stream to evaluate the learner on. Will be restarted if
        ``restart_stream`` is True.
    :param learner: The learner to evaluate.
    :param max_instances: The number of instances to evaluate before exiting. If
        None, the evaluation will continue until the stream is empty.
    :param window_size: The size of the window used for windowed evaluation,
        defaults to 1000
    :param store_predictions: Store the learner's prediction in a list, defaults
        to False
    :param store_y: Store the ground truth targets in a list, defaults to False
    :param optimise: If True and the learner is compatible, the evaluator will
        use a Java native evaluation loop, defaults to True.
    :param restart_stream: If False, evaluation will continue from the current
        position in the stream, defaults to True. Not restarting the stream is
        useful for switching between learners or evaluators, without starting
        from the beginning of the stream.
    :param progress_bar: Enable, disable, or override the progress bar. Currently
        incompatible with ``optimize=True``.
    :param mini_batch: The size of the mini-batch to use for the learner.
    :return: An object containing the results of the evaluation windowed metrics,
        cumulative metrics, ground truth targets, and predictions.
    """
    if restart_stream:
        stream.restart()
    if batch_size != 1 and not isinstance(learner, (BatchClassifier, BatchRegressor)):
        raise ValueError(
            "The learner is not a batch learner, but mini_batch is set to a value greater than 1."
        )
    
    # if _is_fast_mode_compilable(stream, learner, optimise):
    #     return _prequential_evaluation_fast(
    #         stream,
    #         learner,
    #         max_instances,
    #         window_size,
    #         store_y=store_y,
    #         store_predictions=store_predictions,
    #     )

    predictions = None
    if store_predictions:
        predictions = []

    ground_truth_y = None
    if store_y:
        ground_truth_y = []

    drift_detected_index = []

    # Start measuring time
    start_wallclock_time, start_cpu_time = start_time_measuring()

    evaluator_cumulative = None
    evaluator_windowed = None
    if stream.get_schema().is_classification():
        evaluator_cumulative = ClassificationEvaluator(
            schema=stream.get_schema(), window_size=window_size
        )
        if window_size is not None:
            evaluator_windowed = ClassificationWindowedEvaluator(
                schema=stream.get_schema(), window_size=window_size
            )
        
    else:
        if not isinstance(learner, MOAPredictionIntervalLearner):
            evaluator_cumulative = RegressionEvaluator(
                schema=stream.get_schema(), window_size=window_size
            )
            if window_size is not None:
                evaluator_windowed = RegressionWindowedEvaluator(
                    schema=stream.get_schema(), window_size=window_size
                )
        else:
            evaluator_cumulative = PredictionIntervalEvaluator(
                schema=stream.get_schema(), window_size=window_size
            )
            if window_size is not None:
                evaluator_windowed = PredictionIntervalWindowedEvaluator(
                    schema=stream.get_schema(), window_size=window_size
                )

    if cd_ground_truth is not None:
        cd_evaluator = ConceptDriftDetectorEvaluator()

    progress_bar = _setup_progress_bar(
        "Eval", progress_bar, stream, learner, max_instances
    )

    train_instances = list()
    for i, batch in enumerate(batched(islice(stream, max_instances), batch_size)):
        yb_true = [_get_target(instance) for instance in batch]  # batch of targets
        yb_pred = []

        if isinstance(learner, Batch):
            # Collect a batch of instances and predict them all at once
            np_x = np.stack([instance.x for instance in batch])
            torch_x = torch.from_numpy(np_x).to(
                device=learner.device, dtype=learner.x_dtype
            )
            torch_y = torch.tensor(
                yb_true, dtype=learner.y_dtype, device=learner.device
            )
            yb_pred = learner.batch_predict(torch_x).tolist()
            learner.batch_train(torch_x, torch_y)
        else:
            # TODO: Is it correct?
            cd_ground_truth_decision = 0
            if i in cd_ground_truth:
                cd_ground_truth_decision = 1
            for instance in batch:
                # TODO: Is it correct?
                drift_votes = learner.get_cd_votes(instance)
                yb_pred.append(learner.predict(instance))
                train_instances.append(instance)
                if delay_length < len(train_instances):
                    instance_to_train = train_instances.pop(0)
                    learner.train(instance_to_train)
                if drift_votes[0] == 1.0:
                    drift_detected_index.append(i)
                    
                # TODO: Save all metrics from the drift detector
                cd_evaluator.add_result(instance, cd_ground_truth_decision, drift_votes)

        for y_true, y_pred in zip(yb_true, yb_pred, strict=True):
            evaluator_cumulative.update(y_true, y_pred)
            if window_size is not None:
                evaluator_windowed.update(y_true, y_pred)

            # Storing predictions if store_predictions was set to True during initialisation
            if predictions is not None:
                predictions.append(y_pred)

            # Storing ground-truth if store_y was set to True during initialisation
            if ground_truth_y is not None:
                ground_truth_y.append(y_true)

        if progress_bar is not None:
            progress_bar.update(len(batch))

    if progress_bar is not None:
        progress_bar.close()

    # Stop measuring time
    elapsed_wallclock_time, elapsed_cpu_time = stop_time_measuring(
        start_wallclock_time, start_cpu_time
    )

    # Add the results corresponding to the remainder of the stream in case the number of processed
    # instances is not perfectly divisible by the window_size (if it was, then it is already be in
    # the result_windows variable). The evaluator_windowed will be None if the window_size is None.
    if (
        evaluator_windowed is not None
        and evaluator_windowed.get_instances_seen() % window_size != 0
    ):
        evaluator_windowed.result_windows.append(evaluator_windowed.metrics())

    if isinstance(learner, ConceptDriftMethodClassifier):
        learner_name = "HoffdingTree + " + str(learner.drift_detector.__class__.__name__)
    else:
        learner_name = str(learner)

    results = PrequentialResults(
        learner=learner_name,
        stream=stream,
        wallclock=elapsed_wallclock_time,
        cpu_time=elapsed_cpu_time,
        max_instances=max_instances,
        cumulative_evaluator=evaluator_cumulative,
        windowed_evaluator=evaluator_windowed,
        ground_truth_y=ground_truth_y,
        predictions=predictions,
        cd_evaluator=cd_evaluator,
        drift_detected_index=drift_detected_index,
    )

    return results