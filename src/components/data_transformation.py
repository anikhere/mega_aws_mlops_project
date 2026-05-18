import sys 
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from src.exceptions import CustomException
from src.components.data_ingestion import Data_ingestion,Di_Config
from src.logger import logger
import os
@dataclass
class Transformation_Config:
    preprocessor_obj_file = os.path.join('artifacts','preprocessor.pkl')
class DataTranformation:
    def __init__(self,config:Transformation_Config,di:Di_Config):
        self.transform_config = config
        self.di_config = di

    def get_data_trans(self):
        num_cols = [
            'Hours_Studied',
            'Attendance',
            'Sleep_Hours',
            'Previous_Scores',
            'Tutoring_Sessions',
            'Physical_Activity',
            'Exam_Score'
        ]
        cat_cols = [
            'Parental_Involvement',
            'Access_to_Resources',
            'Extracurricular_Activities',
            'Motivation_Level',
            'Internet_Access',
            'Family_Income',
            'Teacher_Quality',
            'School_Type',
            'Peer_Influence',
            'Learning_Disabilities',
            'Parental_Education_Level',
            'Distance_from_Home',
            'Gender'
        ]
        num_pipeline = Pipeline(
            steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ]
        )
        cat_pipeline = Pipeline(
            steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('one_hot', OneHotEncoder()),
                ('scaler', StandardScaler())
            ]
        )
        column_transform = ColumnTransformer(
            [
                ('num_pipe', num_pipeline, num_cols),
                ('cat_pipe', cat_pipeline, cat_cols)
            ]
        )
        return column_transform

    def start_transform(self):
        train_df = pd.read_csv(self.di_config.train_data)
        test_df = pd.read_csv(self.di_config.test_data)
        logger.info('Dataframes are ready')

        preprocessor = self.get_data_trans()

        X_train = train_df.drop(columns=['Exam_Score'], errors='ignore')
        y_train = train_df['Exam_Score'] if 'Exam_Score' in train_df.columns else None
        X_test = test_df.drop(columns=['Exam_Score'], errors='ignore')
        y_test = test_df['Exam_Score'] if 'Exam_Score' in test_df.columns else None

        X_train_transformed = preprocessor.fit_transform(X_train)
        X_test_transformed = preprocessor.transform(X_test)

        return X_train_transformed, X_test_transformed, y_train, y_test, preprocessor