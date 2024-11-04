# import modules
from pathlib import Path
import os
import sys 
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin 


# Add Package Path directory on sys.path to load config.py
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))
print(f'PACKAGE ROOT: {PACKAGE_ROOT}', '\n')

# import config file
from prediction_model.config import config 


# CLASS Domain Processing >> Inherits from BaseEstimator and TransformerMixin
class DomainProcessing(BaseEstimator, TransformerMixin):

    # Initialization >> add new feature (total_assets_value)
    def __init__(self, vars_to_add=None):
        # column name
        self.new_column = config.NEW_FEATURE_ADD
        # features that are going to be added
        self.vars_to_add = vars_to_add

    # fit method
    def fit(self, X, y=None):
        return self 
    
    # transform method
    def transform(self, X):
        # set valu of new col to the sum of var_to_add
        X[self.new_column] = X[self.vars_to_add].sum(axis=1)
        return X 
    

# CLASS Drop Features
class DropFeatures(BaseEstimator, TransformerMixin):

    # initialization >> drop features not neede
    def __init__(self, vars_to_drop=None):
        # fetures to drop
        self.vars_to_drop = vars_to_drop

    # fit method
    def fit(self, X, y=None):
        return self 
    
    # transform method
    def transform(self, X):
        # drop columns
        X = X.drop(columns=self.vars_to_drop)
        return X
    

# CLASS Custom Label Encoder
class CustomLabelEncoder(BaseEstimator, TransformerMixin):

    # initialization >> Dict with categorical vars and their positive class
    def __init__(self, vars=None):
        # Dict with categorical vars and their positive class
        self.vars = vars 

    # fit method
    def fit(self, X, y=None):
        return self
    
    # transform method
    def transform(self, X):
        # iterate through vars dict
        for col_name, posi_value in self.vars.items():
            # lambda >> 1 is positive class
            X[col_name] = X[col_name].apply(lambda x: 1 if x.strip() in posi_value else 0)
        
        return X
    

# CLASS Log Transform
class LogTransform(BaseEstimator, TransformerMixin):

    # initialization >> vars to apply log transform
    def __init__(self, vars=None):
        self.vars = vars 

    # fit method
    def fit(self, X, y=None):
        return self 
    
    # transform method
    def transform(self, X):
        # create copy of X
        X = X.copy()
        
        # iterate through each feature in vars
        for feature in self.vars:
            # apply log transform
            X[feature] = np.log(X[feature])

        return X



