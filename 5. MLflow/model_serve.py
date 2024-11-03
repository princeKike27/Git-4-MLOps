import mlflow

# model name
model_name = 'Loan_Approval_DeciTree_27'

# stage of the model
stage = 'Staging'

# set tracking URI
mlflow.set_tracking_uri('http://127.0.0.1:5000')

# load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(model_uri=f'models:/{model_name}/{stage}')


# Predict on a Pandas DataFrame.
import pandas as pd

# data for prediction
data = [[
            1.0, 0.0, 0.0, 0.0, 0.0, 4.98745, 360.0, 1.0, 2.0, 8.698
        ]]

# predict data
print('\n', f'Prediction on Served Model is: {loaded_model.predict(pd.DataFrame(data))}', '\n')