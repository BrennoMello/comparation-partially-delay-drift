
# import moa.classifiers.core.driftdetection as drift_detection
# import moa.classifiers.trees as moa_trees
from capymoa.drift.base_detector import MOADriftDetector
from capymoa.base import Classifier
# from moa.core import Utils
# from jpype import _jpype
import numpy as np
# import math
import copy



class ConceptDriftMethodClassifier(Classifier):

    def __init__(
        self, 
        schema=None, 
        random_seed=1, 
        drift_detector=None, 
        learner=None,
        loss=None,
    ):
        self.DDM_INCONTROL_LEVEL = 0
        self.DDM_WARNING_LEVEL = 1
        self.DDM_OUTCONTROL_LEVEL = 2

        self.warning_detected = 0
        self.change_detected = 0
        self.new_classifier_reset = False

        self.loss_function = loss() if loss is not None else None

        self.random_seed = random_seed
        self.schema = schema

        self.learner = learner
        self.drift_detector = drift_detector

        self.new_classifier = copy.deepcopy(self.learner)
        self.classifier = copy.deepcopy(self.learner)

        self.classifier.reset()
        self.new_classifier.reset()
        
        self.drift_detection_method = self.drift_detector


    def train(self, instance):
        # instance = instance.java_instance
        true_class = instance.java_instance.getData().classValue()
        predict_class = self.classifier.predict(instance)
        
        # print(f"true_class: {true_class}")
        # print(f"predict_class: {predict_class}")
        
        if predict_class == true_class:
            prediction = True
        else:
            prediction = False

        self.drift_detection_method.add_element(0.0 if prediction else 1.0)
        self.ddmLevel = self.DDM_INCONTROL_LEVEL

        if self.drift_detection_method.detected_change():
            self.ddmLevel = self.DDM_OUTCONTROL_LEVEL
        
        if self.drift_detection_method.detected_warning():
            self.ddmLevel =  self.DDM_WARNING_LEVEL

        if self.ddmLevel == self.DDM_WARNING_LEVEL:
            print("DDM_WARNING_LEVEL")
            if self.new_classifier_reset == True:
                self.warning_detected += 1
                self.new_classifier.reset()
                self.new_classifier_reset = False
            
            self.new_classifier.train(instance)
            

        elif self.ddmLevel == self.DDM_OUTCONTROL_LEVEL:
            print("DDM_OUTCONTROL_LEVEL")
            self.change_detected += 1
            self.classifier = self.new_classifier

            self.new_classifier = copy.deepcopy(self.learner)
            self.new_classifier.reset()
            

        elif self.ddmLevel == self.DDM_INCONTROL_LEVEL:
            # print("DDM_INCONTROL_LEVEL")
            self.new_classifier_reset = True
            
        self.classifier.train(instance)

    def get_classes(self, y_true):
        classes = np.zeros(self.schema.get_num_classes())
        classes[y_true] = 1.0
        return classes
    
    def __str__(self):
        return str("ConceptDriftMethodClassifier")

    def predict(self, instance):
        return self.classifier.predict(instance)

    def predict_proba(self, instance):
        return self.classifier.predict_proba(instance)
    
    #TODO: Update the get output function
    def get_cd_votes(self, instance):
        if isinstance(self.drift_detection_method, MOADriftDetector):
            return self.drift_detection_method.get_votes()
        else:
            drift_votes = [
                1 if self.drift_detection_method.detected_change() else 0,
                1 if self.drift_detection_method.detected_warning() else 0,
                0,
                0
            ]
            
            return drift_votes

    def reset(self):
        
        self.classifier = self.learner.copy()
        self.new_classifier = self.learner.copy()
        self.classifier.reset()
        self.new_classifier.reset()
        
        self.driftDetectionMethod.reset(clean_history=True)
        self.new_classifier_reset = False