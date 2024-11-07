# import modules
from flask import Flask,render_template,request
import joblib
import pandas as pd
import sys
import os
from pathlib import Path

# add path to open model files
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# import config and load_pipeline
from prediction_model.config import config 
from prediction_model.preprocessing.data_handling import load_pipeline

# load trained model
classification_pipeline = load_pipeline(config.MODEL_NAME)

# create instance of Flask
app = Flask(__name__)


# function to transform numeric data to in
def transform_to_integers(data):
    columns_to_convert = [
        'no_of_dependents', 'income_annum', 'loan_amount', 'loan_term', 
        'cibil_score', 'residential_assets_value', 'commercial_assets_value', 
        'luxury_assets_value', 'bank_asset_value' 
    ]

    for col in columns_to_convert:
        try:
            # Attempt to convert the value to an integer
            data[col] = int(data[col])
        except ValueError:
            # Handle the case where conversion fails (e.g., non-numeric value)
            print(f"Warning: Could not convert '{col}' to integer. Value: {data[col]}")

    return data

##############################################################################################

# Home route
@app.route('/') # @ Path Operation decorator
def home():
    return render_template('homepage.html')


# Prediction route
@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        request_data = dict(request.form)
        print(request_data, '\n')

        # turn data into dict with key value pairs
        request_data = {k:v for k,v in request_data.items()}

        # transform to ints
        request_data = transform_to_integers(request_data)
        print(request_data, '\n')

        # create df
        data_df = pd.DataFrame([request_data])
        print(data_df, '\n')

        # prediction
        pred = classification_pipeline.predict(data_df)
        print(f"prediction is {pred}")

        # loan status
        if int(pred[0]) == 1:
            result = "Congratulations! your loan request is approved"
        if int(pred[0]) == 0:
            result = "Sorry! your loan request is rejected"

        # show loan approval result in homepage.html
        return render_template('homepage.html',prediction = result) 


# 500 Error route
@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

# 404 Error route
@app.errorhandler(404)
def not_found(error):
    return "404: Page not found",404


# run if app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)