import os 
import sys
from src.exceptions import CustomException
from src.logger import logger
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
@dataclass
class Di_Config:
    train_data:str=os.path.join('artifacts','train.csv')
    test_data:str=os.path.join('artifacts','test.csv')
    raw_data:str=os.path.join('artifacts','raw.csv')

class Data_ingestion:
    def __init__(self):
        self.di = Di_Config()
    def start_ingestion(self):
        logger.info('Starting data ingestion...')
        try:
          df = pd.read_csv('data/StudentPerformanceFactors.csv')
          os.makedirs(os.path.dirname(self.di.raw_data),exist_ok=True)
          df.to_csv(self.di.raw_data, index=False)
          logger.info('Data saved successfully')
          train_df,test_df = train_test_split(df,test_size=0.2,random_state=42)
          train_csv = train_df.to_csv(self.di.train_data,index=False)
          test_df_csv = test_df.to_csv(self.di.test_data,index=False)
          logger.info(f'finsihed craeting the csvsssss.......')
          return (
              self.di.train_data,
              self.di.test_data
          )
        except Exception as e:
           raise CustomException(e, sys)
obj = Data_ingestion()
obj.start_ingestion()    
        