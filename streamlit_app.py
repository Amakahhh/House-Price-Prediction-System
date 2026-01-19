import streamlit as st
import joblib
import numpy as np
import polars as pl
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="House Price Prediction", layout="centered")

# Load model, scaler, and feature names
BASE_DIR = Path(__file__).parent
MODEL_DIR = BASE_DIR / 'model'

@st.cache_resource
def load_model():
    model = joblib.load(MODEL_DIR / 'house_price_model.pkl')
    scaler = joblib.load(MODEL_DIR / 'scaler.pkl')
    feature_names = joblib.load(MODEL_DIR / 'feature_names.pkl')
    return model, scaler, feature_names

model, scaler, feature_names = load_model()

# App title and description
st.title("🏠 House Price Prediction System")
st.write("Enter property details to predict the house price")

# Create input columns
col1, col2 = st.columns(2)

with col1:
    overall_qual = st.slider("Overall Quality", 1, 10, 5)
    gr_liv_area = st.number_input("Living Area (sq ft)", 300, 5000, 1500)
    total_bsmt_sf = st.number_input("Basement Area (sq ft)", 0, 6000, 1000)

with col2:
    garage_cars = st.slider("Garage Cars", 0, 5, 2)
    year_built = st.number_input("Year Built", 1800, 2024, 2000)
    neighborhood = st.selectbox("Neighborhood", 
                               ['Ames', 'Edwards', 'BriarDale', 'OldTown', 'Sawyer', 
                                'NoRidge', 'NridgHt', 'SomerSet', 'CollgCr'])

# Create prediction button
if st.button("Predict Price", type="primary", use_container_width=True):
    # Prepare input data
    input_data = {
        'OverallQual': overall_qual,
        'GrLivArea': gr_liv_area,
        'TotalBsmtSF': total_bsmt_sf,
        'GarageCars': garage_cars,
        'YearBuilt': year_built,
        'Neighborhood': neighborhood
    }
    
    input_df = pd.DataFrame([input_data])
    input_encoded = pd.get_dummies(input_df, columns=['Neighborhood'], drop_first=True)
    input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)
    input_scaled = scaler.transform(input_encoded)
    prediction = model.predict(input_scaled)[0]
    
    # Display result
    st.success("✅ Prediction Complete!")
    st.metric("Predicted House Price", f"${prediction:,.2f}")
    
    # Show input summary
    st.subheader("Property Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Quality", f"{overall_qual}/10")
    col2.metric("Living Area", f"{gr_liv_area:,.0f} sq ft")
    col3.metric("Year Built", year_built)
