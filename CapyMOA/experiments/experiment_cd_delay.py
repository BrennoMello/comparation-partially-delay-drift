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
)
from capymoa.drift.detectors import (
    ADWIN
)
import numpy as np
from capymoa.stream.generator import AgrawalGenerator
from capymoa.evaluation.visualization import plot_windowed_results

def run_cd_delay_prequential():
    print("START CD EVALUATION PREQUENTIAL DELAY DATA STREAM")
    stream_sea2drift = DriftStream(
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
    
    ht_classifier = HoeffdingTree(schema=stream_sea2drift.get_schema())
    cd_classifier = ConceptDriftMethodClassifier(
        schema=stream_sea2drift.get_schema(),
        drift_detector=ADWIN(),
        learner=ht_classifier,
    )

    results = prequential_cd_delay_evaluation(
        stream=stream_sea2drift,
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
