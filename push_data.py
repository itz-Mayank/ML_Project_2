import os
import sys
import json
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi # To make secure https connection
ce = certifi.where() # CA: Certificate Authority which is trusted

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self,data_path):
        try:
            data = pd.read_csv(data_path)
            data.reset_index(drop=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongodb(self,records,database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    FILE_PATH = os.path.join("Network_Data/phisingData.csv")
    DATABASE = "NETWORK_SECURITY"
    Collection = "NetworkData" # Table in Database
    networkobj = NetworkDataExtract()
    Records = networkobj.csv_to_json_converter(data_path=FILE_PATH)
    print(Records)
    no_of_records = networkobj.insert_data_to_mongodb(Records,DATABASE,Collection)
    print(no_of_records)

