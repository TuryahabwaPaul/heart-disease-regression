from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib  # or whichever method you're using to load your model
import numpy as np  # Import numpy to handle array manipulations

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your model here
model = joblib.load('heart_disease_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Prepare the input data for the model
    input_data = np.array([[data['age'], data['sex'], data['cp'], data['trestbps'], 
                             data['chol'], data['fbs'], data['restecg'], 
                             data['thalach'], data['exang'], data['oldpeak'], 
                             data['slope'], data['ca'], data['thal']]])

    # Make a prediction
    prediction = model.predict(input_data)
    
    # Assuming prediction is an array, get the first element and convert it to a float
    probability = float(prediction[0])  # Change to float if your model outputs an int64

    return jsonify({'probability': probability})

if __name__ == '__main__':
    app.run(debug=True)

