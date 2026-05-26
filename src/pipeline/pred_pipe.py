import sys
import pandas as pd

from src.exceptions import CustomException
from utils import load_object


class PredictPipeline:

    def __init__(self):
        pass


    def predict(self, features):

        try:

            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'

            model = load_object(path=model_path)

            preprocessor = load_object(
                path=preprocessor_path
            )

            data_scaled = preprocessor.transform(features)

            preds = model.predict(data_scaled)

            return preds

        except Exception as e:

            raise CustomException(e, sys)