# import modules
import pytest 
import numpy as np
from pathlib import Path
import os
import sys 


# Add Package Path directory on sys.path to load config.py
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path. append(str(PACKAGE_ROOT))
print(f'PACKAGE ROOT: {PACKAGE_ROOT}', '\n')  

# import files
from prediction_model.config import config
from prediction_model.preprocessing.data_handling import load_dataset, separate_data, load_pipeline


# load model pipeline
classification_pipeline = load_pipeline(config.MODEL_NAME)


# FIXTURES --> functions before test function --> ensure single prediction
@pytest.fixture
def single_prediction():
    # test data
    test_data = load_dataset(config.TEST_FILE)
    # separate X, y
    X, y = separate_data(test_data)
    # predictions
    predi = classification_pipeline.predict(X)
    return predi 


# Test that single prediction is NOT None
def test_single_predi_not_none(single_prediction):
    assert single_prediction is not None


# Test that data type is integer
def test_single_predi_int_type(single_prediction):
    print(f'single_prediction[0]: {single_prediction[0]}, type: {type(single_prediction[0])}')
    assert isinstance(single_prediction[0], np.int64)
