from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import pandas as pd
import numpy as np
import sys,os
import pickle
import dill
import yaml

def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path ,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e

# def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
#     try:
#         dir_path = os.path.dirname(file_path)
#         os.makedirs(dir_path, exist_ok=True)
#         if replace:
#             if os.path.exists(file_path):
#                 os.remove(file_path)
#         # os.makedirs(file_path,exist_ok=True)
#         with open(os.path.dirname(file_path), "w") as file:
#             yaml.dump(content,file)
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        if replace and os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise NetworkSecurityException(e, sys)

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

def save_object(file_path:str,obj:object)->None:
    try:
        logging.info("Entering the save_object method of main utils class")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
        logging.info("Exiting the save_object method of main utils class")
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e