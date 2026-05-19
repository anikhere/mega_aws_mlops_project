from src.components.data_ingestion import *
from src.components.data_transformation import DataTranformation, Transformation_Config
from src.logger import logger
from utils import Save_obj
import yaml
obj = Data_ingestion()
di_config = Di_Config()
obj.start_ingestion()  
trans_config = Transformation_Config()
trans_obj = DataTranformation(config=trans_config,di=di_config)
trans_obj.start_transform()
        