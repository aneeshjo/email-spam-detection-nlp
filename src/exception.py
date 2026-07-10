import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    """
    Returns a detailed error message including
    file name and line number.
    """

    # sys.exc_info() gives us information about the exception that just occurred.
    _,_,exc_tb=error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno


    return  (
        f"Error occurred in Python script: [{file_name}] "
        f"at line number [{line_number}] "
        f"with error message: [{str(error)}]"
    )

    

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):

        return self.error_message




