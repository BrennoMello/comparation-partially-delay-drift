import os
from loguru import logger as log


def run_abrupt_agraw1(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/partially/abrupt_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW1_Abrupt.csv'
                            else:
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                            -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                            -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                            -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                            -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                            -p {size["drift_position"][3]} -w 1) \
                                            -p {size["drift_position"][2]} -w 1) \
                                            -p {size["drift_position"][1]} -w 1) \
                                            -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/partially/abrupt_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW1_Abrupt.csv'
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW1_Abrupt.csv'
                                             
                    
                        log.info(command)
                        os.system(command)

def run_gradual_agraw1(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW1_Gradual.csv'
                                
                            else:        
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW1_Gradual.csv'
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW1_Gradual.csv'           
                        
                        log.info(command)
                        os.system(command)


def run_abrupt_agraw2(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW2_Abrupt.csv'
                            
                            else:    
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW2_Abrupt.csv'
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW2_Abrupt.csv'
                                
                        log.info(command)
                        os.system(command)

def run_gradual_agraw2(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):                                            
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW2_Gradual.csv'
                            else:
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW2_Gradual.csv'    
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                        -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_AGRAW2_Gradual.csv'
                                
                        log.info(command)
                        os.system(command)

def run_abrupt_led(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.LEDGeneratorDrift -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (generators.LEDGeneratorDrift -i {iter} -d 7) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_LED_Abrupt.csv'  
                            else:     
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.LEDGeneratorDrift -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (generators.LEDGeneratorDrift -i {iter} -d 7) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_LED_Abrupt.csv'        
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (generators.LEDGeneratorDrift -i {iter} -d 7) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_LED_Abrupt.csv'
                                
                        log.info(command)
                        os.system(command)

def run_gradual_led(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                            -s (ConceptDriftStream -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                            -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                            -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                            -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (generators.LEDGeneratorDrift -i {iter} -d 7) \
                                            -p {size["drift_position"][3]} -w 500) \
                                            -p {size["drift_position"][2]} -w 500) \
                                            -p {size["drift_position"][1]} -w 500) \
                                            -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_LED_Gradual.csv'    
                            else: 
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                            -s (ConceptDriftStream -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                            -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                            -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                            -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (generators.LEDGeneratorDrift -i {iter} -d 7) \
                                            -p {size["drift_position"][3]} -w 500) \
                                            -p {size["drift_position"][2]} -w 500) \
                                            -p {size["drift_position"][1]} -w 500) \
                                            -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_LED_Gradual.csv'                     
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (ConceptDriftStream \
                                        -s (generators.LEDGeneratorDrift -i {iter} -d 7) -d (generators.LEDGeneratorDrift -i {iter} -d 7) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_LED_Gradual.csv'
                                
                        log.info(command)
                        os.system(command)


def run_abrupt_mixed(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 1) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (generators.MixedGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_MIXED_Abrupt.csv'
                            
                            else:
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 1) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (generators.MixedGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_MIXED_Abrupt.csv'
                        
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 1) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (generators.MixedGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_MIXED_Abrupt.csv'                                
                    
                        log.info(command)
                        os.system(command)


def run_gradual_mixed(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 1) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (generators.MixedGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_MIXED_Gradual.csv'
                            
                            else:
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 1) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (generators.MixedGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_MIXED_Gradual.csv'
                                
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 1) -d (ConceptDriftStream \
                                        -s (generators.MixedGenerator -i {iter} -f 2) -d (generators.MixedGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_MIXED_Gradual.csv'            
                        
                        log.info(command)
                        os.system(command)

def run_abrupt_randomRBF(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 1) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 2) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 3) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 4) -d (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 5) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_RANDOM_RBF_Abrupt.csv'
                                
                            else:
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 1) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 2) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 3) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 4) -d (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 5) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_RANDOM_RBF_Abrupt.csv'
                        
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 1) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 2) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 3) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 4) -d (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 5) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_RANDOM_RBF_Abrupt.csv'       
                        
                        log.info(command)
                        os.system(command)

def run_gradual_randomRBF(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 1) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 2) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 3) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 4) -d (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 5) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_RANDOM_RBF_Gradual.csv'
                            else:
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 1) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 2) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 3) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 4) -d (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 5) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_RANDOM_RBF_Gradual.csv'
                        
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 1) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 2) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 3) -d (ConceptDriftStream \
                                        -s (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 4) -d (generators.RandomRBFGeneratorDrift -i {iter} -c 6 -a 40 -n 50 -r 5) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_RANDOM_RBF_Gradual.csv'
                                                            
                        log.info(command)
                        os.system(command)


def run_abrupt_sine(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 4) -d (generators.SineGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_SINE_Abrupt.csv'
                            else:    
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 4) -d (generators.SineGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_SINE_Abrupt.csv'
                        
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 4) -d (generators.SineGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_SINE_Abrupt.csv'        
                        
                        log.info(command)
                        os.system(command)


def run_gradual_sine(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 4) -d (generators.SineGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_SINE_Gradual.csv'
                            
                            else:    
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 4) -d (generators.SineGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_SINE_Gradual.csv'
                        
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                        -s (generators.SineGenerator -i {iter} -f 4) -d (generators.SineGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_SINE_Gradual.csv'
                        
                        log.info(command)
                        os.system(command)

def run_abrupt_waveform(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (generators.WaveformGeneratorDrift -i {iter} -d 19) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_WAVEFORM_Abrupt.csv'
                                
                            else:
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (generators.WaveformGeneratorDrift -i {iter} -d 19) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_WAVEFORM_Abrupt.csv'
                        
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (generators.WaveformGeneratorDrift -i {iter} -d 19) \
                                        -p {size["drift_position"][3]} -w 1) \
                                        -p {size["drift_position"][2]} -w 1) \
                                        -p {size["drift_position"][1]} -w 1) \
                                        -p {size["drift_position"][0]} -w 1) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/abrupt_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_WAVEFORM_Abrupt.csv'                
                        
                        log.info(command)
                        os.system(command)


def run_gradual_waveform(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for data_partially in size["data_partially"]:
                    for iter in range(repetitions):
                        if(drift_algorithm["params"] != ""):
                            if(drift_algorithm["id"] == "Studd" or drift_algorithm["id"] == "MultivariateDetector"):
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l ({drift_algorithm["drift_name"]} {drift_algorithm["params"]}) \
                                        -s (ConceptDriftStream -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (generators.WaveformGeneratorDrift -i {iter} -d 19) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_WAVEFORM_Gradual.csv'
                                
                            else:
                                command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (generators.WaveformGeneratorDrift -i {iter} -d 19) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_WAVEFORM_Gradual.csv'
                        
                        else:
                            command = f'java -cp moa/src/moa-2023.04.0-sources.jar -javaagent:moa/lib/sizeofag-1.0.4.jar -classpath "moa/lib/*" moa.DoTask "EvaluatePrequentialPartiallyLabeledClassifierConcepDrift -l (moa.classifiers.drift.DetectionConceptDriftMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                        -s (ConceptDriftStream -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (ConceptDriftStream \
                                        -s (generators.WaveformGeneratorDrift -i {iter} -d 19) -d (generators.WaveformGeneratorDrift -i {iter} -d 19) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicPartiallyLabeledConceptDriftPerformanceEvaluator) -i {size["data_size"]} -f 1000 -p {data_partially} -z {iter}" > results/partially/gradual_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{data_partially}_{iter}_WAVEFORM_Gradual.csv'
                        
                        log.info(command)
                        os.system(command)



def run_experiment(repetitions):
    
    #learning_algorithms = ["bayes.NaiveBayes", "trees.HoeffdingTree"]
    learning_algorithms = ["trees.HoeffdingTree"]
    if(repetitions == 30):
        data_stream = [
                       #{"data_size": 10000, "drift_position":  [2000, 2000, 2000, 2000], "data_partially": [99, 98, 97, 96, 95]},   \
                       #{"data_size": 20000, "drift_position": [4000, 4000, 4000, 4000], "data_partially": [99, 98, 97, 96, 95]},    \
                       #{"data_size": 50000, "drift_position": [10000, 10000, 10000, 10000], "data_partially": [99, 98, 97, 96, 95]}, \
                       {"data_size": 100000, "drift_position":[20000, 20000, 20000, 20000], "data_partially": [99, 98, 97, 96, 95]}
                      ]
    else:
        data_stream = [
                       {"data_size": 500000, "drift_position":  [100000, 100000, 100000, 100000], "data_partially": [99, 98, 97, 96, 95]}, \
                       {"data_size": 1000000, "drift_position":  [200000, 200000, 200000, 200000], "data_partially": [99, 98, 97, 96, 95]}, \
                       {"data_size": 2000000, "drift_position": [400000, 400000, 400000, 400000], "data_partially": [99, 98, 97, 96, 95]}    
                      ]    

    drift_detectors_params = [
                            # {"id": "DDM", "drift_name": "DDM", "params": ""},    \
                            # {"id": "EDDM", "drift_name": "EDDM", "params": ""},   \
                            # {"id": "ADWIN", "drift_name": "ADWINChangeDetector", "params": ""},  \
                            # {"id": "ECDD", "drift_name": "EWMAChartDM", "params": ""},   \
                            # {"id": "STEPD", "drift_name": "STEPD", "params": ""},  \
                            # {"id": "SeqDrift2", "drift_name": "SeqDrift2ChangeDetector", "params": ""},  \
                            # {"id": "SEED", "drift_name": "SEEDChangeDetector", "params": ""},   \
                            # {"id": "HDDM_A_Test", "drift_name": "HDDM_A_Test", "params": ""},  \
                            # {"id": "HDDM_W_Test", "drift_name": "HDDM_W_Test", "params": ""},  \
                            #{"id": "FHDDM", "drift_name": "FHDDM", "params": ""},  \
                            #{"id": "FTDD", "drift_name": "FTDD", "params": ""},   \
                            # {"id": "RDDM_30", "drift_name": "RDDM", "params": "-n 30 -w 2 -o 3"}, \
                            # {"id": "RDDM","drift_name": "RDDM", "params": ""},   \
                            #{"id": "WSTD","drift_name": "WSTD", "params": ""},    \
                            # {"id": "HypothesisTestDetectorKs","drift_name": "HypothesisTestDetector", "params": "-h ks"},    \
                            # {"id": "HypothesisTestDetectorWrs","drift_name": "HypothesisTestDetector", "params": "-h wrs"},    \
                            # {"id": "HypothesisTestDetectorTt","drift_name": "HypothesisTestDetector", "params": "-h tt"},    \
                            {"id": "MultivariateDetector","drift_name": "moa.learners.ChangeDetectorEnsembleMultivariateLearner", "params": "-d (PageHinkleyDM -d 0.002) -p 20"},    \
                            {"id": "Studd","drift_name": "moa.learners.StuddLearner", "params": "-b (meta.AdaptiveRandomForest -u  -q -w) -s (meta.AdaptiveRandomForest -u  -q -w) -d (PageHinkleyDM -d 0.002) -w 500"},    \
                            #{"id": "NoChangeDetector","drift_name": "NoChangeDetectorNaive", "params": "-n 1000"}
                            ]
    
                                                
    #log.info(f'Runnig abrupt_agraw1')
    #run_abrupt_agraw1(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    #log.info(f'Runnig gradual_agraw1')
    #run_gradual_agraw1(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    #log.info(f'Runnig abrupt_agraw2')
    #run_abrupt_agraw2(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info('Runnig gradual_agraw2')
    run_gradual_agraw2(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    #log.info(f'Runnig abrupt_led')
    # run_abrupt_led(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig gradual_led')
    # run_gradual_led(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig abrupt_mixed')
    # run_abrupt_mixed(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig gradual_mixed')
    # run_gradual_mixed(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig abrupt_randomRBF')
    # run_abrupt_randomRBF(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig gradual_randomRBF')
    # run_gradual_randomRBF(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig abrupt_sine')
    # run_abrupt_sine(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig gradual_sine')
    # run_gradual_sine(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig abrupt_waveform')
    # run_abrupt_waveform(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig gradual_waveform')
    # run_gradual_waveform(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    # log.info(f'Runnig abrupt_hyperplane')        

if __name__ == "__main__":
    
    run_experiment(repetitions=30)
    #run_experiment(repetitions=10)
    
   