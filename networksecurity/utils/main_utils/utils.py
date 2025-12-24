from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import pandas as pd
import numpy as np
import sys,os
import pickle
import yaml

# Write and Read YAML functions
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        if replace and os.path.exists(file_path):
            os.remove(file_path)
        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    
def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path ,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e


# Save and load numpy array data functions
def save_numpy_array_data(filr_path:str,array = np.array):
    '''
    Docstring for save_numpy_array_data
    
    :param filr_path: Description
    :type filr_path: str
    :param array: Description
    '''
    try:
        dir_path = os.path.dirname(filr_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(filr_path,'wb') as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e

def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
        logging.info("Exiting the load_object method of main utils class.")
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e
    
    
# Save and load object functions
def save_object(file_path:str,obj:object)->None:
    try:
        logging.info("Entering the save_object method of main utils class.")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
        logging.info("Exiting the save_object method of main utils class.")
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e
    
def load_object(file_path:str,obj:object)->None:
    try:
        logging.info("Entering the load_object method of main utils class.")
        if not os.path.exists(file_path):
            raise Exception(f"Th file : {file_path} is not exists.")
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
        logging.info("Exiting the load_object method of main utils class.")
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e
    