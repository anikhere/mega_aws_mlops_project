import sys
class CustomException:
    def __init__(self,error_msg,error_detail:sys):
        super.__init__(error_msg)
        _,_,exec_tb = error_detail.exc_info()
        self.file_name = exec_tb.tb_frame.f_code.co_filename
        self.file_no = exec_tb.tb_lineno

    def __str__(self):
        print(f'the error occured in file{self.file_name}')
        print(f'having the line_no:=={self.file_no}')
        print(f'having the message of{self.args[0]}')
        