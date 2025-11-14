# To handel the Exceptions, we will use this exception.py file.

import sys
# The sys library in Python is used to access system-specific parameters and functions, such as reading command-line arguments, managing the Python runtime environment, and controlling program execution.
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_messege,error_detail:sys):
        self.error_messege = error_messege
        _,_,exc_tb = error_detail.exc_info()
        
        self.lineno = exc_tb.tb_frame.f_code.co_filename
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
        def __str__(self):
            return 'Error occured in python script name [{0}] line number [{1}] error messege[{2}]'.format(self.file_name,self.lineno,str(self.error_messege))
    
# if __name__ == "__main__":
#     try:
#         logger.logging.info("Enter the try block.")
#         a = 1/0
#         print("This will not be printed",a)
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)
    