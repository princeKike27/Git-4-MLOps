# import modules
import mlflow

# set tracking URI
mlflow.set_tracking_uri("http://localhost:5000")

# experiment id
exp_id = mlflow.create_experiment('Loan Prediction')

# starting a run
with mlflow.start_run(run_name='DecisionTreeClass') as run:
    mlflow.set_tag('version', '1.0.1')

# end run
mlflow.end_run()

# logging a parameter from a classifier
n_estimators = 10
criterion = 'gini'
mlflow.log_param('n_estimator', n_estimators)
mlflow.log_param('criterion', criterion)