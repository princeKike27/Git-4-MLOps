# import modules
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib 
import numpy as np
import pandas as pd 
import sys 
import os
from pathlib import Path 

# add path to import trained model
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__)))
print(str(PACKAGE_ROOT), '\n')
sys.path.append(str(PACKAGE_ROOT))

# from prediction_model import
from prediction_model.config import config 
from prediction_model.preprocessing.data_handling import load_pipeline, load_dataset, separate_data 

# load trained model
classification_pipeline = load_pipeline(config.MODEL_NAME) 

# create instance of FastAPI
app = FastAPI()

# parsing with Pydantic
class LoanPred(BaseModel):
    Dependents: int
    Education: str 
    Self_Employed: str 
    TotalIncome: int # income_annum
    LoanAmount: int 
    Loan_Amount_Term: int # loan_term 
    Credit_History: int # cibil_score 
    Residential_Assets_Value: int 
    Commercial_Assets_Value: int 
    Luxury_Assets_Value: int 
    Bank_Asset_Value: int 


# Home Page
@app.get('/')
async def index():
    return {'message': 'Welcome to Loan Prediction App !!!'} 

# Predict
@app.post('/predict')
def predict_loan_status(loan_details: LoanPred):
    # turn user input into a dict 
    data = loan_details.model_dump()
    # new data
    new_data = {
        'no_of_dependents': data['Dependents'],
        'education': data['Education'],
        'self_employed': data['Self_Employed'],
        'income_annum': data['TotalIncome'],
        'loan_amount': data['LoanAmount'],
        'loan_term': data['Loan_Amount_Term'],
        'cibil_score': data['Credit_History'],
        'residential_assets_value': data['Residential_Assets_Value'],
        'commercial_assets_value': data['Commercial_Assets_Value'],
        'luxury_assets_value': data['Luxury_Assets_Value'],
        'bank_asset_value': data['Bank_Asset_Value']
    }

    # new df with a single row from the new_data dict
    new_df = pd.DataFrame([new_data])
    
    # make prediction
    predi = classification_pipeline.predict(new_df) 

    # Rejected
    if predi[0] == 0:
        status_predi = 'Rejected'
    # Approved
    else:
        status_predi = 'Approved'

    return {'Status of Loan Application': status_predi}
    

# run if 
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
