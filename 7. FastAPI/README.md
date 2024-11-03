# Setup Virtual Environment

```python
conda create -n fastapi-env python=3.10
conda activate fastapi-env
pip install -r requirements.txt
```

# Running the Server
`uvicorn main:app --reload`

The command `uvicorn main:app` refers to:
- main: the file main.py (Python "module")
- app: the object created inside of main.py with the line app = FastAPI()
- --reload: make the server restart after code changes. Only used for development
