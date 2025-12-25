from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Python Microservice Running on Kubernetes"}

@app.get("/load")
def cpu_load():
    end = time.time() + 2
    while time.time() < end:
        pass
    return {"status": "CPU load generated"}
