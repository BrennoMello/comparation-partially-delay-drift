from capymoa.evaluation import (
    prequential_cd_delay_evaluation,
    prequential_evaluation,
)
from capymoa.classifier import (
    ConceptDriftMethodClassifier, 
    HoeffdingTree,
)
from capymoa.stream.drift import (
    DriftStream, 
    AbruptDrift,
    GradualDrift,
)
from capymoa.drift.detectors import (
    Hang,
    ADWIN,
    ABCD,  
)
import numpy as np
from capymoa.stream.generator import (
    AgrawalGenerator, LEDGeneratorDrift, RandomRBFGeneratorDrift,
    SineGenerator
)
from capymoa.evaluation.visualization import plot_windowed_results

def data_stream_configuration(repetitions: int):
    learning_algorithms = ["trees.HoeffdingTree"]
    if(repetitions == 30):
        data_stream = [
                       {"data_size": 10000, "drift_position":  [2000, 2000, 2000, 2000], "data_delay": [1000, 2000, 4000, 8000, 10000]},   \
                       {"data_size": 20000, "drift_position": [4000, 4000, 4000, 4000], "data_delay": [1000, 2000, 4000, 8000, 10000]},    \
                       {"data_size": 50000, "drift_position": [10000, 10000, 10000, 10000], "data_delay": [1000, 2000, 4000, 8000, 10000]}, \
                       {"data_size": 100000, "drift_position":[20000, 20000, 20000, 20000], "data_delay": [1000, 2000, 4000, 8000, 10000]}
                      ]
    else:
        data_stream = [
                       {"data_size": 500000, "drift_position":  [100000, 100000, 100000, 100000], "data_delay": [1000, 2000, 4000, 8000, 10000]}, \
                       {"data_size": 1000000, "drift_position":  [200000, 200000, 200000, 200000], "data_delay": [1000, 2000, 4000, 8000, 10000]}, \
                       {"data_size": 2000000, "drift_position": [400000, 400000, 400000, 400000], "data_delay": [1000, 2000, 4000, 8000, 10000]}    
                      ]

    return data_stream, learning_algorithms    

def get_data_stream(repetitions, learning_algorithms, drift_detectors_params, data_stream):
    #abrupt_agraw1
    stream_abrupt_agraw1 = DriftStream(
        stream=[
            AgrawalGenerator(classification_function=1),
            AbruptDrift(position=20000),
            AgrawalGenerator(classification_function=2),
            AbruptDrift(position=40000),
            AgrawalGenerator(classification_function=3),
            AbruptDrift(position=60000),
            AgrawalGenerator(classification_function=4),
            AbruptDrift(position=80000),
            AgrawalGenerator(classification_function=5),
        ]
    )
    #gradual_agraw1
    stream_gradual_agraw1 = DriftStream(
        stream=[
            AgrawalGenerator(classification_function=1),
            GradualDrift(position=20000, width=500),
            AgrawalGenerator(classification_function=2),
            GradualDrift(position=40000, width=500),
            AgrawalGenerator(classification_function=3),
            GradualDrift(position=60000, width=500),
            AgrawalGenerator(classification_function=4),
            GradualDrift(position=80000, width=500),
            AgrawalGenerator(classification_function=5),
        ]
    )
    #abrupt_agraw2
    stream_abrupt_agraw2 = DriftStream(
        stream=[
            AgrawalGenerator(classification_function=6),
            AbruptDrift(position=20000),
            AgrawalGenerator(classification_function=7),
            AbruptDrift(position=40000),
            AgrawalGenerator(classification_function=8),
            AbruptDrift(position=60000),
            AgrawalGenerator(classification_function=9),
            AbruptDrift(position=80000),
            AgrawalGenerator(classification_function=10),
        ]
    )
    #gradual_agraw2
    stream_gradual_agraw2 = DriftStream(
        stream=[
            AgrawalGenerator(classification_function=6),
            GradualDrift(position=20000, width=500),
            AgrawalGenerator(classification_function=7),
            GradualDrift(position=40000, width=500),
            AgrawalGenerator(classification_function=8),
            GradualDrift(position=60000, width=500),
            AgrawalGenerator(classification_function=9),
            GradualDrift(position=80000, width=500),
            AgrawalGenerator(classification_function=10),
        ]
    )
    #abrupt_led
    stream_abrupt_led = DriftStream(
        stream=[
            LEDGeneratorDrift(),
            AbruptDrift(position=20000),
            LEDGeneratorDrift(),
            AbruptDrift(position=40000),
            LEDGeneratorDrift(),
            AbruptDrift(position=60000),
            LEDGeneratorDrift(),
            AbruptDrift(position=80000),
            LEDGeneratorDrift(),
        ]
    )
    #gradual_led
    stream_gradual_led = DriftStream(
        stream=[
            LEDGeneratorDrift(),
            GradualDrift(position=20000, width=500),
            LEDGeneratorDrift(),
            GradualDrift(position=40000, width=500),
            LEDGeneratorDrift(),
            GradualDrift(position=60000, width=500),
            LEDGeneratorDrift(),
            GradualDrift(position=80000, width=500),
            LEDGeneratorDrift(),
        ]
    )

    #abrupt_random_rbf
    stream_abrupt_random_rbf = DriftStream(
        stream=[
            RandomRBFGeneratorDrift(),
            AbruptDrift(position=20000),
            RandomRBFGeneratorDrift(),
            AbruptDrift(position=40000),
            RandomRBFGeneratorDrift(),
            AbruptDrift(position=60000),
            RandomRBFGeneratorDrift(),
            AbruptDrift(position=80000),
            RandomRBFGeneratorDrift(),
        ]
    )
    #gradual_random_rbf
    stream_gradual_random_rbf = DriftStream(
        stream=[
            RandomRBFGeneratorDrift(),
            GradualDrift(position=20000, width=500),
            RandomRBFGeneratorDrift(),
            GradualDrift(position=40000, width=500),
            RandomRBFGeneratorDrift(),
            GradualDrift(position=60000, width=500),
            RandomRBFGeneratorDrift(),
            GradualDrift(position=80000, width=500),
            RandomRBFGeneratorDrift(),
        ]
    )
    

    return [stream_abrupt_agraw1, stream_gradual_agraw1, 
            stream_abrupt_agraw2, stream_gradual_agraw2,
            stream_abrupt_led, stream_gradual_led,
            stream_abrupt_random_rbf, stream_gradual_random_rbf
        ]

def run_cd_delay_prequential():
    print("START CD EVALUATION PREQUENTIAL DELAY DATA STREAM")
    stream_abrupt_agraw1 = DriftStream(
        stream=[
            AgrawalGenerator(classification_function=1),
            AbruptDrift(position=20000),
            AgrawalGenerator(classification_function=2),
            AbruptDrift(position=40000),
            AgrawalGenerator(classification_function=3),
            AbruptDrift(position=60000),
            AgrawalGenerator(classification_function=4),
            AbruptDrift(position=80000),
            AgrawalGenerator(classification_function=5),
        ]
    )

    ht_classifier = HoeffdingTree(schema=stream_abrupt_agraw1.get_schema())
    cd_classifier = ConceptDriftMethodClassifier(
        schema=stream_abrupt_agraw1.get_schema(),
        drift_detector=ABCD(),
        learner=ht_classifier,
    )

    results = prequential_cd_delay_evaluation(
        stream=stream_abrupt_agraw1,
        learner=cd_classifier,
        max_instances=100000,
        delay_length=10000,
        cd_ground_truth=[20000, 40000, 60000, 80000],
    )
    print("Classifier metrics results")
    print(f"learner: {results['learner']} accuracy: {results['cumulative'].accuracy()}")
    print("Concept Drift Detection")
    print(results["drift_detected_index"])
    print("Concept Drift Detection Metrics")
    print(results["cd_evaluator"].get_measurements())

    #results.write_to_file(path="./results")

    #plot_windowed_results(results,  metric="accuracy", plot_title="Delayed labelling (10,000)")
    plot_windowed_results(results,  metric="accuracy", plot_title="No Delay")

if __name__ == "__main__":
    run_cd_delay_prequential()
