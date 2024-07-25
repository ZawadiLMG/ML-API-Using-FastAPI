from fastapi import FastAPI, Query
from pydantic import BaseModel
import pandas as pd
import joblib
import os
import numpy as np

app = FastAPI()

# loading models and encoder
log_reg = joblib.load('../models/logistic_regression_pipeline.pkl')  
SVC = joblib.load('../models/svc_pipeline.pkl')
encoder = joblib.load('../models/label_encoder.pkl')

class DfFeatures(BaseModel):
    prg: int
    pl: int
    pr: int
    sk: int
    ts: int
    m11: float
    bd2: float
    age: int
    insurance: int
    
@app.get('/')
def status_check(
    title: str = Query('Sepsis Prediction API', title='Project Title', description='Title of the project'),
):
    status_message = {
        'api_name': 'Sepsis Prediction API',
        'description': 'This API predicts the likelihood of sepsis based on patient data.',
        'status': 'API is online and functioning correctly.',
        'models_loaded': {
            'logistic_regression_model': 'loaded',
            'svc_model': 'loaded',
            'label_encoder': 'loaded'
        }
    }
    return status_message

@app.post('/predict_sepsis')
def predict_sepsis(data: DfFeatures, model: str = Query('log_reg', enum=['log_reg', 'svc'])):
    df = pd.DataFrame([data.model_dump()])

    # Select the model based on the query parameter
    if model == 'log_reg':
        prediction = log_reg.predict(df)
        probability = log_reg.predict_proba(df)
    elif model == 'SVC':
        prediction = SVC.predict(df)
        probability = SVC.predict_proba(df)
    
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])[0]
    probability = probability[0]

    return {
        'model_used': model,
        'prediction': prediction,
        'probability': f'The probability of the prediction is {probability[0]:.2f}'
    }