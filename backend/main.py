from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import Optional
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and scaler
model = joblib.load('heart_disease_model.joblib')
scaler = joblib.load('scaler.joblib')

class HealthData(BaseModel):
    age: int
    sex: int  # 1 = male, 0 = female
    cp: int   # chest pain type (0-3)
    trestbps: int  # resting blood pressure
    chol: int     # serum cholesterol
    fbs: int      # fasting blood sugar
    restecg: int  # resting ECG results
    thalach: int  # maximum heart rate achieved
    exang: int    # exercise induced angina
    oldpeak: float # ST depression induced by exercise
    slope: int    # slope of the peak exercise ST segment
    ca: int       # number of major vessels colored by flourosopy
    thal: int     # thalassemia type

    @validator('age')
    def validate_age(cls, v):
        if v < 0 or v > 120:
            raise ValueError('Age must be between 0 and 120')
        return v

    @validator('trestbps')
    def validate_blood_pressure(cls, v):
        if v < 50 or v > 300:
            raise ValueError('Blood pressure must be between 50 and 300')
        return v

@app.post("/predict")
async def predict(data: HealthData):
    try:
        # Convert input data to numpy array
        features = np.array([[
            data.age, data.sex, data.cp, data.trestbps,
            data.chol, data.fbs, data.restecg, data.thalach,
            data.exang, data.oldpeak, data.slope, data.ca,
            data.thal
        ]])
        
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict_proba(features_scaled)[0][1]
        
        # Get feature importance
        feature_importance = dict(zip(
            ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
             'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'],
            model.feature_importances_
        ))
        
        return {
            "prediction": float(prediction),
            "risk_level": "High" if prediction > 0.5 else "Low",
            "feature_importance": feature_importance
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}