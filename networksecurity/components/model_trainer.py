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

# Main Utils
from networksecurity.utils.main_utils.utils import save_object, load_object, load_numpy_array_data, evaluate_models

# ML Algorithms
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig,
                 data_transformation_artifact: DataTransformationArtifacts):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
            logging.info(f"{'>>'*20} Model Trainer {'<<'*20}")
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def train_model(self,x_train,y_train,x_test,y_test):
        models = {
            "Random Forest": RandomForestClassifier(verbose=1),
            "Decision Tree": DecisionTreeClassifier(),
            "Gradient Boosting": GradientBoostingClassifier(verbose=1),
            "Logistic Regression" : LinearRegression(),
            "AdaBoost": AdaBoostClassifier(),
        }
        params = {
            "Random Forest": {
                'n_estimators': [8,16,32,64,128,256],
                # 'max_depth': [None, 10, 20],
            },
            "Decision Tree": {
                'criterion': ['gini', 'entropy','log_loss'],
                # 'max_depth': [None, 10, 20],
            },
            "Gradient Boosting": {
                'learning_rate': [0.01, 0.1, 0.5, 0.001],
                'subsample' : [0.6,0.7,0.75,0.8,0.85,0.9],
                'n_estimators': [8,16,32,64,128,256],   
            },
            "Logistic Regression" : {},
            "AdaBoost": {
                'learning_rate': [0.01, 0.1, 0.5, 0.001],
                'n_estimators': [8,16,32,64,128,256],
            },
        }
        
        # To generate model report
        model_report:dict = evaluate_models(x_train = x_train, y_train = y_train, x_test = x_test, y_test = y_test,
                                            models = models, params = params)
        
        # Best model score
        best_model_score = max(sorted(model_report.values()))
        
        # Best model name
        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]
        
        # Best model
        best_model = models[best_model_name]
        
        # Result of train
        y_train_pred = best_model.predict(x_train)
        classification_train_metric = get_classification_score(y_true = y_train, y_pred = y_train_pred)
        
        ## Track the experiements with mlflow
        # self.track_mlflow(best_model,classification_train_metric)
        
        # Result of test
        y_test_pred = best_model.predict(x_test)
        classification_test_metric = get_classification_score(y_true = y_test, y_pred = y_test_pred)
        
        logging.info("Saving the trained model object")
        preprocessor = load_object(
            file_path = self.data_transformation_artifact.transformed_object_file_path
        )
        model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
        os.makedirs(model_dir_path, exist_ok = True)
        
        network_model = NetworkModel(preprocessor = preprocessor, model = best_model)

        save_object(
            file_path=self.model_trainer_config.trained_model_file_path,
            obj=network_model
        )

        model_trainer_artifact = ModelTrainerArtifact(
            trained_model_file_path=self.model_trainer_config.trained_model_file_path,
            train_metric_artifact=classification_train_metric,
            test_metric_artifact=classification_test_metric
        )

        logging.info(f"Model Trainer Artifact: {model_trainer_artifact}")
        return model_trainer_artifact
        
    
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
            
            model_trainer_artifact=self.train_model(x_train,y_train,x_test,y_test)
            return model_trainer_artifact


        except Exception as e:
            raise NetworkSecurityException(e, sys) from e