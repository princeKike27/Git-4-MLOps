# import modules
from sklearn.pipeline import Pipeline
from pathlib import Path
import os
import sys 
import numpy as np
from sklearn.linear_model import LogisticRegression



# Add Package Path directory on sys.path to load config.py
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
print(f'PACKAGE ROOT: {PACKAGE_ROOT}', '\n')

# import config file
from prediction_model.config  import config 
# import preprocessing file
from prediction_model.preprocessing import preprocessing as pp


# Pipeline steps
classification_pipeline = Pipeline(
    [
        ('DomainProcessing', pp.DomainProcessing(vars_to_add=config.FEATURE_TO_ADD)),
        ('DropFeatures', pp.DropFeatures(vars_to_drop=config.DROP_FEATURES)),
        ('LabelEncoder', pp.CustomLabelEncoder(vars=config.FEATURES_TO_ENCODE)),
        ('LogTransform', pp.LogTransform(vars=config.LOG_FEATURES)),
        ('LogisticClassifier', LogisticRegression(random_state=0))
    ]
)