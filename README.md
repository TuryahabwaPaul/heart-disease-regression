# Heart Disease Prediction Web Application

![Heart Disease Prediction](img1.PNG) <!-- Add a path to your image here -->

A modern web application that predicts heart disease risk using machine learning. Built with React, Flask, and Random Forest Classifier.

## Features ✨

- **Real-time Predictions**: Get instant heart disease risk assessments
- **User-friendly Interface**: Clean, responsive design built with React
- **Secure API**: RESTful Flask backend with CORS protection
- **Advanced ML Model**: Random Forest Classifier trained on comprehensive healthcare data
- **Interactive Visualization**: Dynamic charts showing prediction results
- **Form Validation**: Comprehensive input validation with instant feedback

## Tech Stack 🛠️

### Frontend
- React 18+
- Custom CSS
- Axios for API calls

### Backend
- Flask 2.0+
- scikit-learn for ML operations
- pandas & numpy for data processing
- Flask-CORS for security

## Getting Started 🚀

### Prerequisites

- Python 3.8 or higher
- Node.js 14.0 or higher
- pip (Python package manager)
- npm (Node package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/TuryahabwaPaul/heart-disease-regression.git
cd heart-disease-regression
```

2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install Python dependencies
pip install flask
pip install flask-cors
pip install pandas
pip install numpy
pip install scikit-learn
pip install joblib
pip install gunicorn

python app.py
```
Server will run on `http://localhost:5000`

3. Frontend Setup
```bash
cd frontend
npm install
npm start
```
Application will run on `http://localhost:3000`

## Project Structure 📁

```
heart-disease-predictor/
├── backend/
│   ├── app.py                 # Flask application
│   ├── model/
│   │   ├── classifier.pkl     # Trained model
│   │   └── training.ipynb     # Model training notebook
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── services/         # API services
│   │   └── styles/           # CSS files
│   ├── package.json
│   └── README.md
└── README.md
```