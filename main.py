from src.components.data_ingestion import *
from src.components.data_transformation import DataTranformation, Transformation_Config
from src.components.model_trainer import Model_config,Model_trainer
from src.logger import logger
from utils import Save_obj
import yaml
obj = Data_ingestion()
di_config = Di_Config()
obj.start_ingestion()  
trans_config = Transformation_Config()
trans_obj = DataTranformation(config=trans_config,di=di_config)
train_arr,test_arr,pre_obj = trans_obj.start_transform()
model_config = Model_config()
model_trainer = Model_trainer(model_config)
best_model = model_trainer.start_training(train_arr=train_arr,test_arr=test_arr)