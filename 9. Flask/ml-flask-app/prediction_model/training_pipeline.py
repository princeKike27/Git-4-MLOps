# import modules
import pandas as pd
import numpy as np
from pathlib import Path 
import os 
import sys 

# Add Package Path directory on sys.path to load config.py
PACKAGE_ROOT =Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
print(f'PACKAGE ROOT: {PACKAGE_ROOT}', '\n') 

# import files
from prediction_model.config import config 
from prediction_model.preprocessing import preprocessing as pp
import prediction_model.pipeline as pipe
from prediction_model.preprocessing.data_handling import load_dataset, separate_data, split_data, save_pipeline


# Function to perform training
def perform_training():
    # load dataset
    dataset = load_dataset(config.FILE_NAME)
    # separate data
    X, y = separate_data(dataset) 
    # encode y
    y = y.apply(lambda y: 1 if y.strip() == 'Approved' else 0 )
    # train test split
    x_train, x_test, y_train, y_test = split_data(X, y)

    # TEST DATA
    test_data = x_test.copy()
    test_data[config.TARGET] = y_test 
    # save to csv
    test_data.to_csv(os.path.join(config.DATAPATH, config.TEST_FILE))

    # Train Pipeline
    pipe.classification_pipeline.fit(x_train, y_train)

    # Save Pipeline
    save_pipeline(pipe.classification_pipeline)


# Run Training if we are in training_pipeline.py
if __name__ == '__main__':
    perform_training() 