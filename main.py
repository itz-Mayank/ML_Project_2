from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation

from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import os
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        
        # Data Ingestion
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion.")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed.")
        print(dataingestionartifact)
        
        # Data Validation
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the Data Validation.")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation completed.")
        print(data_validation_artifact)
        
        # Data transformation
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        logging.info("Initiate the Data Transformation.")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation completed.")
        print(data_transformation_artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e