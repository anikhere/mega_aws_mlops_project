import os 
import yaml
import pandas as pd
import dill
from sklearn.metrics import r2_score
def yaml_open(path:str)-> dict:
    with open(path,'r') as file:
        content = yaml.safe_load(file)
        return content
def save_csv(path:str,save_path:str)->None:
    df = pd.read_csv(path)
    df.to_csv(save_path,index=False)
def Save_obj(obj,model_path):
    dirname = os.path.dirname(model_path)
    os.makedirs(dirname,exist_ok=True)
    with open(model_path,'wb') as file:
        dill.dump(obj,file)
def evaluate_model(models,x_train,y_train,x_test,y_test):
    report = {}
    for i in range(len(list(models))):
        model = list(models.values())[i]
        model.fit(x_train,y_train)
        pred = model.predict(x_test)
        score = r2_score(y_test,pred)
        report[list(models.keys())[i]] = score
        
    
    return report

