import os 
import yaml
import pandas as pd
def yaml_open(path:str)-> dict:
    with open(path,'r') as file:
        content = yaml.safe_load(file)
        return content
def save_csv(path:str,save_path:str)->None:
    df = pd.read_csv(path)
    df.to_csv(save_path,index=False)
