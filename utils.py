import os 
import yaml
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
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
def evaluate_model(models,x_train,y_train,x_test,y_test,params):
    report = {}
    for i in range(len(list(models))):
        para = params[list(models.keys())[i]]
        
        model = list(models.values())[i]
        gs = GridSearchCV(
            estimator=model,
            param_grid=para,
            cv=3,
            n_jobs=-1,
            verbose=True,
            refit=True
        )
        gs.fit(x_train, y_train)
        best_model = gs.best_estimator_
        print("i am the best:", best_model)

        models[list(models.keys())[i]] = best_model
        pred = best_model.predict(x_test)
        score = r2_score(y_test,pred)
        report[list(models.keys())[i]] = score
        
    
    return report
def load_object(path:str):
    with open(path,'rb') as file:
        model = dill.load(file)
        return model

