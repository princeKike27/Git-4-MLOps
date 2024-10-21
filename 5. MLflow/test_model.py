import mlflow
logged_model = 'runs:/9e4b1d3630c143029aed457135c407f9/RandomForestClassifier'


# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd

# data for prediction
data = [[
            1.0, 0.0, 0.0, 0.0, 0.0, 4.98745, 360.0, 1.0, 2.0, 8.698
        ]]

# predict data
print(f'Prediction is: {loaded_model.predict(pd.DataFrame(data))}')