import pandas as pd
import pickle
import yaml
from sklearn.metrics import accuracy_score
import os
import mlflow
from urllib.parse import urlparse

os.environ['MLFLOW_TRACKING_URI']='https://dagshub.com/ad94kaz/machine-learning-pipeline.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME']='ad94kaz'
os.environ['MLFLOW_TRACKING_PASSWORD']='ab53143af8959c0da7e3139e28debf9f08c6b3ac'

# Load parameters from params.yaml
params=yaml.safe_load(open('params.yaml'))['train']

def evaluate(data_path,model_path):
    data=pd.read_csv(data_path)
    X = data.drop(columns=['Outcome'])
    y = data['Outcome']

    mlflow.set_tracking_uri('https://dagshub.com/ad94kaz/machine-learning-pipeline.mlflow')

    ## Load the model from the disk
    model=pickle.load(open(model_path,'rb'))

    predictions=model.predict(X)
    accuracy = accuracy_score(y,predictions)

    # Log metrics to MLflow
    mlflow.log_metric('accuracy',accuracy)
    print('Model accuracy:{accuracy}')

if __name__=='__main__':
    evaluate(params['data'],params['model'])