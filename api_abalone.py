import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd
from abalone_model import abalone

app = FastAPI()
pickle_in = open('model.pkl', 'rb')
regressor = pickle.load(pickle_in)

@app.get("/")
def index():
    return {"message": "Halo, Pak Ade"}

@app.post("/predict")
def predict(data: abalone):
    data = data.dict()
    
    # Manual encoding untuk kolom 'Sex'
    sex_mapping = {'M': 0, 'F': 1, 'I': 2}
    Sex = sex_mapping.get(data['Sex'], -1)
    
    Length = data['Length']
    Diameter = data['Diameter']
    Height = data['Height']
    Whole_weight = data['Whole_weight']
    Whole_weight_1 = data['Whole_weight_1']
    Whole_weight_2 = data['Whole_weight_2']
    Shell_weight = data['Shell_weight']
    
    prediction = regressor.predict([[Sex, Length, Diameter, Height, Whole_weight, Whole_weight_1, Whole_weight_2, Shell_weight]])
    
    result = int(prediction[0])
    return {
        "prediction": result
    }
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# cd ./abalone/ -> buat masuk ke folder directory abalone (opt)
# uvicorn api_abalone:app --reload

# python -m venv env
# ./env/Scripts/activate.bat -> aktifin venv
# pip install uvicorn fastapi pandas numpy pydantic scikit-learn

