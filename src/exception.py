from src.logger import logging
import sys

def get_error_message(error_message,sys_:sys):
    _,_,tb = sys_.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    logging.info(f"We encountered an error on line {tb.tb_lineno} in file {file_name}")
    return f"There is an error in {file_name}, on line number: {tb.tb_lineno} the message we got is: {str(error_message)}"

class CustomException(Exception):
    def __init__(self, error_message, sys_):
        self.sys_ = sys_
        self.error_message = get_error_message(error_message, sys_)

    def __str__(self):
        return self.error_message
    
if __name__ == '__main__':
    try:
        print(1/0)
    except Exception as e:
        raise CustomException(e,sys)