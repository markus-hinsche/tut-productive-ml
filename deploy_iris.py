from fastapi import FastAPI, Request
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


def check_params(query_params):
    assert "sepal length" in query_params, query_params
    assert "sepal width" in query_params, query_params
    assert "petal length" in query_params, query_params
    assert "petal width" in query_params, query_params


# Define the /prediction route
@app.get('/predict/', response_model=Prediction)
async def predict_route(req: Request):
    query_params = dict(req.query_params)
    check_params(query_params)
    data = [
        query_params["sepal length"],
        query_params["sepal width"],
        query_params["petal length"],
        query_params["petal width"],
    ]
    pred = clf2.predict([data])
    return {"data": pred}


# Define the /prediction route
@app.post('/prediction/', response_model=Prediction)
async def prediction_route(item: Item):
    pred = clf2.predict([item.data])
    return {"data": pred}
