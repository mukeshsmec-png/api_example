
from fastapi import FastAPI
import uvicorn

app =FastAPI()

@app.get("/add")
def add(x,y):
    return x+y

@app.get("/sub")
def sub(x,y):
    return x-y

import sys 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=9321)

