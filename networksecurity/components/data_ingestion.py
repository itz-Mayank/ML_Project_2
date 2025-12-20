from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


# Configuration of the data ingestion config
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifacts_entity import DataIngestionArtifacts

import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()
n,m 0

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    # Exporting the data from the mongodb
    def export_collection_as_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            
            logging.info("Exporting data from mongodb")
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            logging.info("Connected to Mongodb successfully")
            
            database = self.mongo_client[database_name]
            collection = database[collection_name]
            
            data = pd.DataFrame(list(collection.find()))
            if "_id" in data.columns.to_list():
                data = data.drop(columns=["_id"],axis=1)
            data.replace({"na":np.nan},inplace=True)
            
            logging.info("Data exported from Mongodb successfully")
            return data
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    # Export data into feature Store
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info("Exporting data into feature store")
            dataframe.to_csv(feature_store_file_path,index=False, header=True)
            logging.info("Data exported into feature store successfully")
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    # Split the data into train and test file
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_file_path = self.data_ingestion_config.train_file_path
            test_file_path = self.data_ingestion_config.test_file_path
            
            dir_path = os.path.dirname(train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dir_path = os.path.dirname(test_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            logging.info("Splitting data into train and test file")
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )
            train_set.to_csv(train_file_path,index=False,header=True)
            test_set.to_csv(test_file_path,index=False,header=True)
            logging.info("Data split into train and test file successfully")
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            data_ingestion_artifact = DataIngestionArtifacts(
                # feature_store_file_path = self.data_ingestion_config.feature_store_file_path,
                train_file_path = self.data_ingestion_config.train_file_path,
                test_file_path = self.data_ingestion_config.test_file_path
            )
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)