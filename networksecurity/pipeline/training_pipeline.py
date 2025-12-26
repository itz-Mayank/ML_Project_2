# Similar to the main.py file
import sys,os

# Exception and Logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Components
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

# Config Entity
from networksecurity.entity.config_entity import (
        TrainingPipelineConfig,
        DataIngestionConfig,
        DataValidationConfig,
        DataTransformationConfig,
        ModelTrainerConfig
    )

# Artifacts Entity
from networksecurity.entity.artifacts_entity import (
        DataIngestionArtifacts,
        DataValidationArtifacts,
        DataTransformationArtifacts,
        ModelTrainerArtifact,
        # TrainingPipelineArtifacts
    )

class TrainingPipeline:
    def __init__(self):
        try:
            self.training_pipeline_config = TrainingPipelineConfig()
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
    
    def start_data_ingestion(self)-> DataIngestionArtifacts:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Completed data ingestion")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
    
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifacts)->DataValidationArtifacts:
        try:
            self.data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data validation")
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                            data_validation_config=self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Completed data validation")
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e

    def start_data_transformation(self,data_validation_artifact:DataValidationArtifacts)->DataTransformationArtifacts:
        try:
            self.data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data transformation")
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
                                                    data_transformation_config=self.data_transformation_config)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info("Completed data transformation")
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e

    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifacts)->ModelTrainerArtifact:
        try:
            self.model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting model trainer")
            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact,
                                        model_trainer_config=self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            logging.info("Completed model trainer")
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifacts = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            return model_trainer_artifacts
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e