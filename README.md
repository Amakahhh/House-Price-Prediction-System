# House Price Prediction System

A machine learning-based web application that predicts house prices using advanced regression techniques.

## 📋 Project Overview

This project implements a complete house price prediction system consisting of:
- **Model Development**: Random Forest Regressor trained on the House Prices dataset
- **Web Interface**: Flask-based GUI for user-friendly predictions
- **Model Persistence**: Joblib-based model serialization

## 🏗️ Project Structure

```
House Price Prediction System/
├── model/
│   ├── model_building.ipynb          # Model development notebook
│   ├── house_price_model.pkl         # Trained model
│   ├── scaler.pkl                    # Feature scaler
│   └── feature_names.pkl             # Feature column names
├── templates/
│   └── index.html                    # Web interface template
├── static/
│   └── style.css                     # CSS styling
├── app.py                            # Flask application
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## 🎯 Features

- **6 Key Features Used**:
  - OverallQual (Overall Quality)
  - GrLivArea (Ground Living Area)
  - TotalBsmtSF (Total Basement Area)
  - GarageCars (Garage Size)
  - YearBuilt (Year Built)
  - Neighborhood (Location)

- **Machine Learning Algorithm**: Random Forest Regressor
- **Model Performance**:
  - Trains on 80% of data, tests on 20%
  - Calculates MAE, MSE, RMSE, and R² metrics
  - High accuracy predictions

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for version control)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "House Price Prediction System"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Model Development

### Running the Jupyter Notebook

1. Open the `model_building.ipynb` notebook in your Jupyter environment
2. The notebook will:
   - Load the House Prices dataset from Kaggle
   - Handle missing values
   - Perform feature selection and encoding
   - Scale features using StandardScaler
   - Train the Random Forest model
   - Evaluate performance metrics
   - Save the model and supporting files

### Key Steps

1. **Data Preprocessing**: Missing value handling, categorical encoding
2. **Feature Engineering**: Select 6 features from 9 recommended
3. **Model Training**: Random Forest with 100 estimators
4. **Evaluation**: Comprehensive metrics (MAE, MSE, RMSE, R²)
5. **Model Persistence**: Save using Joblib

## 🌐 Web Application

### Running the Flask App Locally

```bash
python app.py
```

The app will be available at `http://localhost:5000`

### Features

- **Input Form**: Enter property details
- **Real-time Prediction**: Get instant price predictions
- **Responsive Design**: Works on desktop and mobile
- **Error Handling**: Robust error messages

## 📈 Model Details

- **Algorithm**: Random Forest Regressor
- **Number of Trees**: 100
- **Max Depth**: 20
- **Training/Test Split**: 80/20
- **Scaler**: StandardScaler (mean=0, std=1)
- **Model Persistence**: Joblib (.pkl files)

## 🔄 Model Reloading

The saved model can be reloaded without retraining:

```python
import joblib

model = joblib.load('model/house_price_model.pkl')
scaler = joblib.load('model/scaler.pkl')
features = joblib.load('model/feature_names.pkl')

# Make predictions
predictions = model.predict(scaled_features)
```

## 🚢 Deployment

### Option 1: Render.com

1. Push code to GitHub
2. Connect GitHub repository to Render
3. Set Python runtime to 3.10+
4. Install dependencies: `pip install -r requirements.txt`
5. Run command: `gunicorn app:app`

### Option 2: PythonAnywhere

1. Create account at pythonyanywhere.com
2. Upload files via web interface or Git
3. Create web app with Python 3.10
4. Set WSGI configuration to point to `app.py`
5. Reload the app

### Option 3: Streamlit Cloud

Modify app to use Streamlit:

```bash
pip install streamlit
streamlit run streamlit_app.py
```

Push to GitHub and connect to Streamlit Cloud.

### Option 4: Vercel (requires restructuring)

Convert Flask app to Serverless functions for Vercel deployment.

## 📝 API Endpoints

### `/` (GET)
Returns the main web interface

### `/predict` (POST)
Makes a house price prediction

**Request Body:**
```json
{
  "OverallQual": 7,
  "GrLivArea": 1500,
  "TotalBsmtSF": 1000,
  "GarageCars": 2,
  "YearBuilt": 2000,
  "Neighborhood": "Ames"
}
```

**Response:**
```json
{
  "success": true,
  "prediction": 180000.50,
  "formatted_prediction": "$180,000.50"
}
```

### `/api/info` (GET)
Returns model information

### `/health` (GET)
Health check endpoint

## 🔧 Troubleshooting

### Model Not Found Error
- Ensure `model_building.ipynb` has been run completely
- Check that all files are in the `model/` directory

### Port 5000 Already in Use
```bash
python app.py --port 5001
```

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

## 📚 Technologies Used

- **Backend**: Flask, Python 3.8+
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: HTML5, CSS3, JavaScript
- **Model Serialization**: Joblib
- **Data Science**: Jupyter Notebook

## 📊 Evaluation Metrics

The model is evaluated using:
- **MAE (Mean Absolute Error)**: Average absolute prediction error
- **MSE (Mean Squared Error)**: Average squared prediction error
- **RMSE (Root Mean Squared Error)**: Square root of MSE
- **R² Score**: Coefficient of determination (0-1)

## 🤝 Contributing

To improve the model:
1. Adjust hyperparameters in the notebook
2. Try different algorithms (SVR, Linear Regression, Prophet)
3. Feature engineering improvements
4. Cross-validation implementation

## 📄 License

Educational project for CSC 415 - AI Course

## 👤 Author

[Your Name]
Matric Number: [Your Matric Number]

## 📞 Support

For issues or questions about the model, refer to the Jupyter notebook documentation.

---

**Last Updated**: January 2026
