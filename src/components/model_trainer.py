import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from utils import evaluate_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exceptions import CustomException
from src.logger import logging
from utils import Save_obj
from src.components.data_transformation import DataTranformation
@dataclass
class Model_config:
    model_path: str=os.path.join('artifacts','model.pkl')
class Model_trainer:
    def __init__(self,config:Model_config,):
        self.config = config
    def start_training(self,train_arr,test_arr):
        x_train = train_arr[:, :-1]
        y_train = train_arr[:, -1]

        x_test = test_arr[:, :-1]
        y_test = test_arr[:, -1]
        models = {
            "Random Forest": RandomForestRegressor(),
            "Decision Tree": DecisionTreeRegressor(),
            "Gradient Boosting": GradientBoostingRegressor(),
            "Linear Regression": LinearRegression(),
            "K-Neighbors Classifier": KNeighborsRegressor(),
            "XGBClassifier": XGBRegressor(),
            "CatBoosting Classifier": CatBoostRegressor(verbose=False),
            "AdaBoost Classifier": AdaBoostRegressor(),
            }
        model_report:dict = evaluate_model(models=models,x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test)
        best_score = max(model_report.values())  
        best_model_name = list(model_report.keys())[list(model_report.values()).index(best_score)]
        best_model = models[best_model_name]
        

        if best_score < 0.6:
            raise CustomException(f'no best model found')
        
        Save_obj(model_path=self.config.model_path,
                 obj=best_model
        
        )
        return best_model
