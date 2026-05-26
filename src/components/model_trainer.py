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
        params = {

            "Random Forest": {
                "n_estimators": [50, 100, 200],
                "max_depth": [None, 10, 20, 30],
                "min_samples_split": [2, 5, 10],
                "min_samples_leaf": [1, 2, 4],
            },

            "Decision Tree": {
                "criterion": ["squared_error", "friedman_mse"],
                "max_depth": [None, 10, 20, 30],
                "min_samples_split": [2, 5, 10],
                "min_samples_leaf": [1, 2, 4],
            },

            "Gradient Boosting": {
                "n_estimators": [50, 100, 200],
                "learning_rate": [0.01, 0.05, 0.1],
                "max_depth": [3, 5, 7],
                "subsample": [0.8, 1.0],
            },

            "Linear Regression": {
                # usually no important hyperparameters
            },

            "K-Neighbors Classifier": {
                "n_neighbors": [3, 5, 7, 9],
                "weights": ["uniform", "distance"],
                "algorithm": ["auto", "ball_tree", "kd_tree"],
            },

            "XGBClassifier": {
                "n_estimators": [50, 100, 200],
                "learning_rate": [0.01, 0.05, 0.1],
                "max_depth": [3, 5, 7],
                "subsample": [0.8, 1.0],
                "colsample_bytree": [0.8, 1.0],
            },

            "CatBoosting Classifier": {
                "iterations": [100, 200],
                "learning_rate": [0.01, 0.05, 0.1],
                "depth": [4, 6, 8],
            },

            "AdaBoost Classifier": {
                "n_estimators": [50, 100, 200],
                "learning_rate": [0.01, 0.05, 0.1, 1.0],
            }
        }
        model_report:dict = evaluate_model(models=models,x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test,params = params)
        best_score = max(model_report.values())  
        best_model_name = list(model_report.keys())[list(model_report.values()).index(best_score)]
        best_model = models[best_model_name]
        
        

        if best_score < 0.6:
            raise CustomException(f'no best model found')
        print("Best model name:", best_model_name)
        print("Best score:", best_score)
        print("Best model object:", best_model)
        Save_obj(model_path=self.config.model_path, obj=best_model)
        
        

        return best_model
