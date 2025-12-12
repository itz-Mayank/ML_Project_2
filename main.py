from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import os
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion.")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed.")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the Data Validation.")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation completed.")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)