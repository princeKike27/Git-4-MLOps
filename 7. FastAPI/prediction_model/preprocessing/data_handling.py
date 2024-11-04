# import modules
import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from pathlib import Path
import sys


# Add Package Path directory on sys.path to load config.py
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))
print(f'PACKAGE ROOT: {PACKAGE_ROOT}', '\n')

# import config file
from prediction_model.config import config


# LOAD DATASET
def load_dataset(file_name, train=True):
    # filepath of file
    filepath = os.path.join(config.DATAPATH, file_name)
    print(f'Data filepath: {filepath}')
    # load data
    _data = pd.read_csv(filepath)
    # remove leading spaces from col names
    _data.columns = [name.strip() for name in _data.columns]
    # return data
    return _data[config.FEATURES]


# SEPARATE X AND Y
def separate_data(data):
    X = data.drop(config.TARGET, axis=1)
    y = data[config.TARGET] 
    return X, y


# SPLIT DATA
def split_data(X, y, test_size=0.2, random_state=42):
    # split in train and test
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return x_train, x_test, y_train, y_test


# SERIALIZATION >> Saving the Model
def save_pipeline(pipeline_to_save):
    # path to save
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    print(f'save_path: {save_path}')
    # save model
    joblib.dump(pipeline_to_save, save_path)
    print(f'Model has been saved under the name: {config.MODEL_NAME}') 


# DESERIALIZATION >> Loading the Model
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    # load model
    loaded_model = joblib.load(save_path)
    print(f'Model has been loaded')
    return loaded_model
    
