from fastapi import FastAPI

from src.bmi import *

# FastAPIのインスタンスを作成
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/bmi/")
async def get_bmi(height: float, weight: float):
    return {"bmi": bmi(height, weight)}
