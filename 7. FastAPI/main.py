# import fastapi
from fastapi import FastAPI 

# create FastAPI instance >> main point of interaction 
app = FastAPI()

# Home Page
@app.get('/') #@ Path Operation Decorator >> Takes the function below and performs an action
async def root(): # called by FastAPI when it receives the request for the URL
    return {'message': 'Hello World from FASTAPI'}

# Demo page
@app.get('/demo')
def demo_func():
    return {'message': 'This is a message from demo function'}


# Post_Demo page
@app.post('/post_demo')
def demo_post():
    return {'message': 'This is an output from post_demo function'}