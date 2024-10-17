# import modules
import os
import mlflow

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics 


# load dataset
df = pd.read_csv('https://raw.githubusercontent.com/manifoldailearning/Complete-MLOps-Bootcamp-v2/refs/heads/main/MLFlow-Manage-ML-Experiments/train.csv')
# numerical cols
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
# categorical cols
cate_cols = df.select_dtypes(include=['object']).columns.tolist()
# remove cols
cate_cols.remove('Loan_Status')
cate_cols.remove('Loan_ID')

# fill na in cate_cols with mode
for col in cate_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# fill na in num_cols with median
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# take care of outliers
df[num_cols] = df[num_cols].apply(lambda x: x.clip(*x.quantile([0.05, 0.95])))

# Log Transforms and Domain Processing
df['LoanAmount'] = np.log(df['LoanAmount']).copy()
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']
df['TotalIncome'] = np.log(df['TotalIncome']).copy()

# drop ApplicantIncome and CoapplicantIncome
df = df.drop(columns=['ApplicantIncome', 'CoapplicantIncome'])


# Label Encoding
for col in cate_cols:
    # create LabelEncoder instance
    le = LabelEncoder()
    # encode cols
    df[col] = le.fit_transform(df[col])

# encode target col
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])


# ----------------------------------------------------------------------------------------

# set X and y
X = df.drop(columns=['Loan_Status', 'Loan_ID'])
y = df['Loan_Status']
RANDOM_SEED = 6 

# train test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_SEED)

########################################################################
# RandomForest
rand_for = RandomForestClassifier(random_state=RANDOM_SEED)

# param grid
param_grid_forest = {
    'n_estimators': [200, 400, 700],
    'max_depth': [10, 20, 30],
    'criterion': ['gini', 'entropy'],
    'max_leaf_nodes': [50, 100]
}

# forest grid
grid_forest = GridSearchCV(
    estimator=rand_for,
    param_grid=param_grid_forest,
    cv=5,
    n_jobs=1,
    scoring='accuracy',
    verbose=0
)

# train model
model_forest = grid_forest.fit(x_train, y_train)

########################################################################
# Logistic Regression
log_reg = LogisticRegression(random_state=RANDOM_SEED)

# param grid
param_grid_log = {
    'C': [100, 10, 1.0, 0.1, 0.01],
    'penalty': ['l1','l2'],
    'solver':['liblinear']
}

# log grid
grid_log = GridSearchCV(
        estimator=log_reg,
        param_grid=param_grid_log, 
        cv=5,
        n_jobs=-1,
        scoring='accuracy',
        verbose=0
    )

# train model
model_log = grid_log.fit(x_train, y_train)

########################################################################
# DecisionTree
deci_tree = DecisionTreeClassifier(random_state=RANDOM_SEED)

# param grid
param_grid_tree = {
    "max_depth": [3, 5, 7, 9, 11, 13],
    'criterion' : ["gini", "entropy"],
}

# tree grid
grid_tree = GridSearchCV(
        estimator=deci_tree,
        param_grid=param_grid_tree, 
        cv=5,
        n_jobs=-1,
        scoring='accuracy',
        verbose=0
    )

# train model
model_tree = grid_tree.fit(x_train, y_train)

########################################################################

# set mlflow experiment
mlflow.set_experiment('Loan_Prediction_27')


# EVAL_METRICS function
def eval_metrics(actual, predi):
    # accuracy
    accuracy = metrics.accuracy_score(actual, predi)
    # f1
    f1 = metrics.f1_score(actual, predi, pos_label=1)
    # fpr, tpr
    fpr, tpr, _ = metrics.roc_curve(actual, predi)
    # auc
    auc = metrics.auc(fpr, tpr)

    # plot roc curve
    plt.figure(figsize=(8, 8))
    plt.plot(fpr, tpr, color='blue', label=f'ROC Curve AUC = {np.round(auc, 2)}')
    # diagonal line
    plt.plot([0, 1], [0, 1], 'r--')
    # limits and labels
    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.xlabel('False Positive Rate', size=14)
    plt.ylabel('True Positive Rate', size=14)
    plt.legend(loc='lower right')

    # save plot in dir
    os.makedirs('plots', exist_ok=True)
    plt.savefig('plots/ROC_curve.png')

    # close plot
    plt.close()
    return (accuracy, f1, auc)



# MLFLOW_LOGGING function
def mlflow_logging(model, x_test, y_test, model_name):
    # start mlflow run
    with mlflow.start_run() as run:
        # get run id
        run_id = run.info.run_id
        # set tag for each run
        mlflow.set_tag('run_id', run_id)

        # get prediction
        predi = model.predict(x_test)
        # calculate metrics 
        (accuracy, f1, auc) = eval_metrics(y_test, predi)

        # log BEST params from gridsearch
        mlflow.log_params(model.best_params_)

        # log metrics
        mlflow.log_metric('Mean CV score', model.best_score_)
        mlflow.log_metric('Accuracy', accuracy)
        mlflow.log_metric('f1-score', f1)
        mlflow.log_metric('AUC', auc)

        # log artifact and model
        mlflow.log_artifact('plots/ROC_curve.png')
        mlflow.sklearn.log_model(model, model_name)

        # end run
        mlflow.end_run()


# run mlflow_logging
mlflow_logging(model_tree, x_test, y_test, 'DecisionTreeClassifier')
mlflow_logging(model_log, x_test, y_test, 'LogisticRegression')
mlflow_logging(model_forest, x_test, y_test, 'RandomForestClassifier')
