# FastAPI Boilerplate
## A simle start point for any FastAPI application.
> Use the codebase for creating and running a FastAPI project in just seconds. Use the complete code base or use any code section you need.

The following featured are included. (Yet more to come.)
### Features:
1. [Setting Up application.](#setting-up)
2. Basic Usage
3. Routing
4. Configuration
5. Validation
6. CRUD Operations
7. DataBase (SQLite, Postgres, MongoDB)
8. DataBase Migration
9. SQLAlchemy
10. Documentation
11. API testing
12. Unit Testing
13. Deployment
---
## Setting Up
### Setting up virtual environment
Clone the codebase or create from scratch. If you crate from scratch, create a folder. Open the folder directory in the terminal. Make sure have python installed in your machine. To create a virtual environment use the following command.
```shell
python -m venv virtalEnvName
```
Go for any `virtualEnvName` you like. It should create a folder in the `name`. Now you need to activate the virtual environment. Run the following command
```shell
cd virtalEnvName\Scripts
activate
```
To deactivate the virtual environment, run the following command
```shell
deactivate
```
### Install FastAPI
Run the following command
```shell
pip install fastapi[all]
```
It will install FastAPI with all the dependencies.
### Create a ```main.py``` file
Add the following code section in the ```main.py``` file.
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome from FastAPI"}
```
### Run the server
You will also need an ASGI server, for production such as *Uvicorn*. Run the following command (if not have *uvicorn* already):
```
pip install "uvicorn[standard]"
``` 
If already installed, run the server with the following command:
```
uvicorn main:app --reload
```
Here ```main``` is the name of your python file and ```app``` is the variable the FastAPI is initialized into. 
> Make sure to change directory to the folder where `main.py` is and run the command in there.

The server should be up and running now. check [http://127.0.0.1:8000](http://127.0.0.1:8000)
Check the Documentation from [API Documentation](http://127.0.0.1:8000/docs)
