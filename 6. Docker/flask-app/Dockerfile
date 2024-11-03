FROM python:3.8

# set directory for the app
WORKDIR /usr/src/app 

# copy all the files to the container
COPY . .

# install dependencies 
RUN pip install --no-cahe-dir -r requirements.txt 

# tell the port number the container should expose
EXPOSE 5001 

# run the command
CMD ["python", "./app.py"]

