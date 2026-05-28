import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
from src.pipeline.pred_pipe import PredictPipeline
templates = Jinja2Templates(directory="templates")
pred = PredictPipeline()
@app.get('/')
async def home_page(request:Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={
            'name':'taha',
            'role':'ceo'
        }
    )
from pydantic import BaseModel


class CustomData(BaseModel):
    Hours_Studied: int
    Attendance: int
    Sleep_Hours: int
    Previous_Scores: int
    Tutoring_Sessions: int
    Physical_Activity: int
    Parental_Involvement: str
    Access_to_Resources: str
    Extracurricular_Activities: str
    Motivation_Level: str
    Internet_Access: str
    Family_Income: str
    Teacher_Quality: str
    School_Type: str
    Peer_Influence: str
    Learning_Disabilities: str
    Parental_Education_Level: str
    Distance_from_Home: str
    Gender: str

@app.post('/predict')
async def predictor(request:Request, data:CustomData):
    data_dict = {key:[value] for key,value in data.model_dump().items()}
    df = pd.DataFrame(data=data_dict)
    result = pred.predict(df)
    return {"prediction": float(result[0])}
from mangum import Mangum
application = Mangum(app)