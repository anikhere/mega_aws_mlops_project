import os 
from dataclasses import dataclass
@dataclass
class Data_valid_artifact:
    valid_train_csv:str
    valid_test_csv:str
    valid_report:str