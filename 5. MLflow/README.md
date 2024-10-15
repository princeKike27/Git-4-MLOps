## Virtual Environment
Create Virtual Environment with Conda

```
conda create -n mlflow_venv python=3.10
conda activate mlflow-env
pip install mlflow
```

- To check commands of mlflow: 
    - `mlflow`

<br>

- To launch UI in local port
    - `mlfow ui`

<br>

### Functions on MLflow Tracking

- `mlflow.set_tracking_uri()`
    - connects to a tracking URI. 
    - You can also set the MLFLOW_TRACKING_URI environment variable to have MLflow find a URI from there. 
    - In both cases, the URI can either be a HTTP/HTTPS URI for a remote server, a database connection string, or a local path to log data to a directory. 
    - The URI defaults to mlruns.

<bR>

- `mlflow.get_tracking_uri()`
    - Returns the current tracking URI

<br>

- `mlflow.create_experiment()`
    - Creates a new experiment and returns its ID
    - Runs can be launched under the experiment by passing the experiment ID to `mlflow.start_run()`

<bR>

- `mlflow.set_experiment()`
    - Sets an experiment as active
    - If the experiment does not exist, creates a new experiment
    - If you don't specify an experiment in `mlflow.start_run()`, new runs are launche dunder this experiment

<br>

- `mlflow.start_run()`
    - Returns the currently active run (if one exists)
    - Or it starts a new run and returns a `mlflow.ActiveRun` object usable as a context manager for the current run

<br>

- `mlflow.log_param()`
    - Logs a SINGLE key-value param in the currently active run
    - The key and the value are both strings
    - Use `mlflow.log_params()` to log multiple params at once

<bR>

- `mlflow.log_metric()`
    - Logs a SINGLE key-value metric
    - The value must always be a number
    - MLflow remembers the history of values for each metric
    - Use `mlflow.log_metrics` to log multiple parameters at once

<br>

- `mlflow.set_tag()`
    - Sets a single key-value tag in the currently active run
    - The key and the value are both strings

<br>

- `mlflow.log_artifact()`
    - Logs a local file or directory as an artifact, 
    - Optionally taking an `artifact_path` to place it within the run's artifact URI
    - Run artifacts can be organized into directories 

<br>

- `mlflow.log_artifacts()`
    - Logs ALL the files in a given directory as Artifacts
    - Optionally it can take an `artifact_path`