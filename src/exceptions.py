import sys
from src.logger import logger

class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        _, _, exc_tb = error_detail.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.file_no = exc_tb.tb_lineno

    def __str__(self):
        return (f'Error in file: {self.file_name}, '
                f'line: {self.file_no}, '
                f'message: {self.args[0]}')

if __name__ == "__main__":
    try:
        value = 10/0
        print(value)
    except Exception as e:
        logger.info('cant print this')
        raise CustomException(str(e), sys)