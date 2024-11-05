# import modules
import pandas as pd
import numpy as np
from pathlib import Path 
import os
import sys

# Add Package Path directory on sys.path to load config.py
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
print(f'PACKAGE ROOT: {PACKAGE_ROOT}', '\n')  

# import files
from prediction_model.config import config 
from prediction_model.preprocessing.data_handling import load_pipeline, load_dataset, separate_data

# load model pipeline
classification_pipeline = load_pipeline(config.MODEL_NAME)

# Function to generate predictions
def generate_predictions():
    # load test data
    test_data = load_dataset(config.TEST_FILE)
    # separate data
    X, y = separate_data(test_data)
    # predictions
    predi = classification_pipeline.predict(X)
    # output label
    predi_label = np.where(predi==1, 'Approved', 'Not Approved')
    print(f'Predicted Label:')
    print(predi_label)

    return predi_label 


# Run generate_predictions if we are in predict.py
if __name__ == '__main__':
    generate_predictions()
