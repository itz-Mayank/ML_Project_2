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
