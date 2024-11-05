# import modueñs
import joblib
import streamlit as st
import pandas as pd
import sys
import os
from pathlib import Path

# add path to be able to access prediction_model dir
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# import config
from prediction_model.config import config 
# import load_pipeline
from prediction_model.preprocessing.data_handling import load_pipeline

# load trained model
classification_pipeline = load_pipeline(config.MODEL_NAME)


# PREDICTION function
def predi_func(Dependents,Education,SelfEmployed,AnnualIncome,LoanAmount,
               LoanAmountTerm,CibilScore,ResidentialAssetsValue,CommercialAssetsValue,
               LuxuryAssetsValue,BankAssetsValue):
    
    # new data
    data = {
        'no_of_dependents': Dependents, 
        'education': Education, 
        'self_employed': SelfEmployed, 
        'income_annum': AnnualIncome, 
        'loan_amount': LoanAmount, 
        'loan_term': LoanAmountTerm, 
        'cibil_score': CibilScore, 
        'residential_assets_value':ResidentialAssetsValue , 
        'luxury_assets_value': LuxuryAssetsValue, 
        'bank_asset_value': BankAssetsValue,
        'commercial_assets_value':CommercialAssetsValue 
    } 

    # create df
    data_df = pd.DataFrame(data, index=[0])
    # predict loan approval
    predi = classification_pipeline.predict(data_df)
    print(predi) 

    # prediction status
    if predi[0] == 0:
        status_predi = 'Rejected'
    else:
        status_predi = 'Approved'

    return status_predi

##########################################################################################
# MAIN function
def main():
    # front-end
    st.title("Welcome to Loan Application")
    st.header("Please enter your details to proceed with your loan Application")

    Dependents = st.number_input("Number of Dependents")
    Education = st.selectbox("Education",("Graduate","Not Graduate"))
    SelfEmployed = st.selectbox("Self Employed",("Yes","No"))
    AnnualIncome = st.number_input("Applicant Income")
    LoanAmount = st.number_input("LoanAmount")
    LoanAmountTerm = st.number_input("Loan Amount Term (in years)")
    CibilScore = st.number_input("Cibil Score")
    ResidentialAssetsValue = st.number_input("Residential Assets Value")
    CommercialAssetsValue = st.number_input("Commercial Assets Value")
    LuxuryAssetsValue = st.number_input("Luxury Assets Value")
    BankAssetsValue = st.number_input("Bank Assets Value")

    # button
    if st.button('Predict Loan Approval'):
        # store prediction from predi_func
        result = predi_func(Dependents,Education,SelfEmployed,AnnualIncome,LoanAmount,
                            LoanAmountTerm,CibilScore,ResidentialAssetsValue,CommercialAssetsValue,
                            LuxuryAssetsValue,BankAssetsValue)
        
        if result == 'Approved':
            st.success('Your Loan Application is Approved')
        else:
            st.error('Your Loan Application is Rejected')


# run if main function if
if __name__ == '__main__':
    main()

