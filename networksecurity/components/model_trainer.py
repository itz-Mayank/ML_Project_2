import sys,os
import numpy as np
import pandas as pd

# Exception and Logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Entities
from networksecurity.entity.artifacts_entity import DataTransformationArtifacts, ModelTrainerArtifact
from networksecurity.entity.config_entity import ModelTrainerConfig

# ML utils
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score

from networksecurity.utils.main_utils.utils import save_object, load_object, load_numpy_array_data

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig,
                 data_transformation_artifact: DataTransformationArtifacts):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
            logging.info(f"{'>>'*20} Model Trainer {'<<'*20}")
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def train_model(self,x_train,y_train):
        
    
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info("Loading transformed training and testing datasets")
            train_array = load_numpy_array_data(
                self.data_transformation_artifact.transformed_train_file_path
            )
            test_array = load_numpy_array_data(
                self.data_transformation_artifact.transformed_test_file_path
            )

            logging.info("Splitting input and target features")
            x_train = train_array[:, :-1]
            y_train = train_array[:, -1]

            x_test = test_array[:, :-1]
            y_test = test_array[:, -1]
            
            logging.info("Training the model")
            model = self.train_model(x_train,y_train)
            from sklearn.ensemble import RandomForestClassifier
            model = RandomForestClassifier()
            model.fit(x_train, y_train)

            logging.info("Evaluating the model")
            y_pred = model.predict(x_test)

            classification_metric = get_classification_score(y_true=y_test, y_pred=y_pred)
            logging.info(f"Model evaluation metrics: {classification_metric}")

            logging.info("Saving the trained model object")
            preprocessor = load_object(
                self.data_transformation_artifact.transformed_object_file_path
            )
            network_model = NetworkModel(preprocessor=preprocessor, model=model)

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=network_model
            )

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                classification_metric=classification_metric
            )

            logging.info(f"Model Trainer Artifact: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e