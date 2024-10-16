# import modules
import os
import mlflow
import argparse
import time 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import numpy as np
import pandas as pd



# LOAD_DATA function
def load_data():
    # url
    URL = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
    
    try:
        # read csv
        df = pd.read_csv(URL, sep=';')
        return df 
    except Exception as e:
        raise e


# EVAL function
def eval_function(actual_val, predi_val):
    # metrics
    rmse = mean_squared_error(actual_val, predi_val)
    mae = mean_absolute_error(actual_val, predi_val)
    r2 = r2_score(actual_val, predi_val)

    return rmse, mae, r2



# MAIN function
def main(alpha, l1_ratio):
    # load dataset
    df = load_data()

    # set X and Y
    TARGET = 'quality'
    X = df.drop(columns=TARGET)
    y = df[TARGET]

    # split data
    x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=6, test_size=0.2)

    # set mlflow experiment
    mlflow.set_experiment('ML-Model-27')

    # start mlflow run
    with mlflow.start_run():
        # log params
        mlflow.log_param('alpha', alpha)
        mlflow.log_param('l1_ratio', l1_ratio)

        # create model instance
        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=6)
        # train model
        model.fit(x_train, y_train)
        # prediction
        y_pred = model.predict(x_test)

        # get eval metrics
        rmse, mae, r2 = eval_function(y_test, y_pred)
        # log metrics
        mlflow.log_metric('rmse', rmse)
        mlflow.log_metric('mae', mae)
        mlflow.log_metric('r2', r2) 

        # log model >> (model, folder_name)
        mlflow.sklearn.log_model(model, "trained_model")





# receive parameters from command line
if __name__ == '__main__':
    # create parser
    args = argparse.ArgumentParser()
    # read input from user
    args.add_argument('--alpha', "-a", type=float, default=0.2)
    args.add_argument('--l1_ratio', "-l1", type=float, default=0.3)
    # parsed arguments
    parsed_args = args.parse_args() # access param 1 >> parsed_args.param1
    # pass inputs from command line to main function
    main(parsed_args.alpha, parsed_args.l1_ratio)