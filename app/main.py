from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from xgboost import XGBClassifier

app = FastAPI()

user_integer = None

# Query params vs Path params

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/get_prediction/")
def enter_features(features):
    processed_features = process_features(features)
    prediction = predict(processed_features)
    return prediction  

def load_dummy_model():
    # return a dummy model trained on fake data
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    labels = [0, 1, 0]
    model = XGBClassifier()
    model.fit(data, labels)    
    return model
    

def load_model():
    model = XGBClassifier()
    model.load_model("model.json")   
    return model
    
def load_scaler():
    model = StandardScaler()
    model.load_model("path_to_scaler")
    return model

def process_features(features):
    # load scaler model
    
    # one hot encoding, scaling, etc
    return features

def predict(features):
    model = load_dummy_model()
    prediction = model.predict_proba(features)
    return prediction