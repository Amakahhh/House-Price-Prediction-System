from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os
from pathlib import Path

app = Flask(__name__)

# Get the absolute path to the model directory
BASE_DIR = Path(__file__).parent
MODEL_DIR = BASE_DIR / 'model'

# Initialize model, scaler, and feature_names as None
model = None
scaler = None
feature_names = None

# Load the trained model, scaler, and feature names
try:
    model_path = MODEL_DIR / 'house_price_model.pkl'
    scaler_path = MODEL_DIR / 'scaler.pkl'
    feature_names_path = MODEL_DIR / 'feature_names.pkl'
    
    if model_path.exists() and scaler_path.exists() and feature_names_path.exists():
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        feature_names = joblib.load(feature_names_path)
        print("✓ Model loaded successfully!")
        print(f"✓ Feature names: {feature_names}")
    else:
        print("✗ Model files not found")
        if not model_path.exists():
            print(f"  Missing: {model_path}")
        if not scaler_path.exists():
            print(f"  Missing: {scaler_path}")
        if not feature_names_path.exists():
            print(f"  Missing: {feature_names_path}")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    import traceback
    traceback.print_exc()
    print("Please run train_model.py to train and save the model.")

# Define the original features used in the model
ORIGINAL_FEATURES = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'GarageCars', 'YearBuilt', 'Neighborhood']
NEIGHBORHOODS = ['Ames', 'Edwards', 'BriarDale', 'OldTown', 'Sawyer', 'NoRidge', 'NridgHt', 'SomerSet', 'CollgCr']

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html', neighborhoods=NEIGHBORHOODS)

@app.route('/predict', methods=['POST'])
def predict():
    """Make a prediction based on user input"""
    try:
        # Check if model is loaded
        if model is None or scaler is None or feature_names is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded. Please ensure model files are present.'
            }), 500
        
        # Get JSON data from the request
        data = request.get_json()
        
        # Extract features from input
        features_dict = {
            'OverallQual': float(data.get('OverallQual', 5)),
            'GrLivArea': float(data.get('GrLivArea', 1500)),
            'TotalBsmtSF': float(data.get('TotalBsmtSF', 1000)),
            'GarageCars': float(data.get('GarageCars', 2)),
            'YearBuilt': float(data.get('YearBuilt', 2000)),
            'Neighborhood': str(data.get('Neighborhood', 'Ames'))
        }
        
        # Create a DataFrame with the features
        input_df = pd.DataFrame([features_dict])
        
        # Encode categorical variables (Neighborhood)
        input_encoded = pd.get_dummies(input_df, columns=['Neighborhood'], drop_first=True)
        
        # Ensure the input has the same columns as the model was trained with
        input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)
        
        # Scale the features
        input_scaled = scaler.transform(input_encoded)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Return the prediction as JSON
        return jsonify({
            'success': True,
            'prediction': float(prediction),
            'formatted_prediction': f"${prediction:,.2f}"
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/info', methods=['GET'])
def get_info():
    """Get model information"""
    return jsonify({
        'algorithm': 'Random Forest Regressor',
        'features': ORIGINAL_FEATURES,
        'neighborhoods': NEIGHBORHOODS,
        'feature_count': len(feature_names)
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for deployment"""
    return jsonify({'status': 'healthy', 'message': 'House Price Prediction API is running'})

if __name__ == '__main__':
    # Use environment variable for PORT (required for deployment)
    # Default to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    # Set debug=False for production/deployment safety
    app.run(host='0.0.0.0', port=port, debug=False)
