# https://www.machinecurve.com/index.php/2020/03/19/tutorial-how-to-deploy-your-convnet-classifier-with-keras-and-fastapi/#loading-the-model-and-getting-input-shape

from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load


clf2 = load('iris.p')

# Define the FastAPI app
app = FastAPI()

class Prediction(BaseModel):
    data: int

class Item(BaseModel):
    data: list

# Define the main route
@app.get('/')
def root_route():
    return { 'error': 'Use GET /prediction instead of the root route!' }


# Define the /prediction route
@app.post('/prediction/', response_model=Prediction)
async def prediction_route(item: Item):
    pred = clf2.predict([item.data])
    return {"data": pred}
