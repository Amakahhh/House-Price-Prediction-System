"""
House Price Prediction Model Training Script
This script trains the model without requiring Jupyter Notebook
Run this with: python train_model.py
"""

import pandas as pd
import numpy as np
import os
import sys
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("HOUSE PRICE PREDICTION MODEL - TRAINING SCRIPT")
print("=" * 80)

# Step 1: Import required libraries
print("\n[1/10] Importing libraries...")
try:
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    import joblib
    print("✓ All libraries imported successfully!")
except ImportError as e:
    print(f"✗ Error importing libraries: {e}")
    sys.exit(1)

# Step 2: Load the dataset
print("\n[2/10] Loading dataset...")
try:
    # Try multiple sources
    sources = [
        'https://raw.githubusercontent.com/awesomedata/awesome-public-datasets/master/datasets/Kaggle/train.csv',
        'https://kaggle.com/c/house-prices-advanced-regression-techniques/data',
    ]
    
    train_data = None
    for url in sources:
        try:
            train_data = pd.read_csv(url)
            print(f"✓ Dataset loaded from {url}! Shape: {train_data.shape}")
            break
        except:
            continue
    
    if train_data is None:
        # If URLs fail, create synthetic data for demonstration
        print("⚠ Using synthetic data (generate real data from Kaggle for production)")
        np.random.seed(42)
        n_samples = 1460
        train_data = pd.DataFrame({
            'OverallQual': np.random.randint(1, 11, n_samples),
            'GrLivArea': np.random.randint(334, 5642, n_samples),
            'TotalBsmtSF': np.random.randint(0, 6110, n_samples),
            'GarageCars': np.random.randint(0, 5, n_samples),
            'BedroomAbvGr': np.random.randint(0, 9, n_samples),
            'FullBath': np.random.randint(0, 4, n_samples),
            'YearBuilt': np.random.randint(1872, 2011, n_samples),
            'Neighborhood': np.random.choice(['Ames', 'Edwards', 'BriarDale', 'OldTown', 'Sawyer', 'NoRidge', 'NridgHt', 'SomerSet', 'CollgCr'], n_samples),
        })
        # Create target with some correlation to features
        train_data['SalePrice'] = (
            train_data['OverallQual'] * 25000 +
            train_data['GrLivArea'] * 100 +
            train_data['TotalBsmtSF'] * 50 +
            train_data['GarageCars'] * 15000 +
            (train_data['YearBuilt'] - 1872) * 500 +
            np.random.normal(0, 20000, n_samples)
        ).astype(int)
        print(f"✓ Synthetic dataset created! Shape: {train_data.shape}")
except Exception as e:
    print(f"✗ Error loading dataset: {e}")
    print("Please download the dataset from Kaggle: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data")
    sys.exit(1)

# Step 3: Display basic info
print("\n[3/10] Exploring dataset...")
recommended_features = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'GarageCars', 'BedroomAbvGr', 'FullBath', 'YearBuilt', 'Neighborhood', 'SalePrice']
print(f"Dataset shape: {train_data.shape}")
print(f"Missing values in recommended features:")
print(train_data[recommended_features].isnull().sum())

# Step 4: Handle missing values
print("\n[4/10] Handling missing values...")
for col in recommended_features:
    if train_data[col].isnull().sum() > 0:
        if train_data[col].dtype == 'object':
            train_data[col].fillna(train_data[col].mode()[0], inplace=True)
        else:
            train_data[col].fillna(train_data[col].mean(), inplace=True)
print("✓ Missing values handled!")

# Step 5: Feature selection and preparation
print("\n[5/10] Selecting features and splitting data...")
selected_features = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'GarageCars', 'YearBuilt', 'Neighborhood']
target = 'SalePrice'

X = train_data[selected_features].copy()
y = train_data[target].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"✓ Features selected: {selected_features}")
print(f"  Training set: {X_train.shape[0]} samples")
print(f"  Test set: {X_test.shape[0]} samples")

# Step 6: Encode categorical variables
print("\n[6/10] Encoding categorical variables...")
categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()
X_train_encoded = pd.get_dummies(X_train, columns=categorical_cols, drop_first=True)
X_test_encoded = pd.get_dummies(X_test, columns=categorical_cols, drop_first=True)
X_test_encoded = X_test_encoded.reindex(columns=X_train_encoded.columns, fill_value=0)
print(f"✓ Categorical variables encoded!")
print(f"  Total features after encoding: {X_train_encoded.shape[1]}")

# Step 7: Scale features
print("\n[7/10] Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_encoded)
X_test_scaled = scaler.transform(X_test_encoded)
print("✓ Features scaled using StandardScaler!")

# Step 8: Train model
print("\n[8/10] Training Random Forest model...")
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_scaled, y_train)
print("✓ Model trained successfully!")

# Step 9: Evaluate model
print("\n[9/10] Evaluating model performance...")
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

train_mae = mean_absolute_error(y_train, y_train_pred)
train_mse = mean_squared_error(y_train, y_train_pred)
train_rmse = np.sqrt(train_mse)
train_r2 = r2_score(y_train, y_train_pred)

test_mae = mean_absolute_error(y_test, y_test_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)
test_r2 = r2_score(y_test, y_test_pred)

print("\n" + "=" * 80)
print("MODEL PERFORMANCE METRICS")
print("=" * 80)
print("\nTRAINING SET:")
print(f"  MAE:  ${train_mae:,.2f}")
print(f"  MSE:  ${train_mse:,.2f}")
print(f"  RMSE: ${train_rmse:,.2f}")
print(f"  R²:   {train_r2:.4f}")

print("\nTEST SET:")
print(f"  MAE:  ${test_mae:,.2f}")
print(f"  MSE:  ${test_mse:,.2f}")
print(f"  RMSE: ${test_rmse:,.2f}")
print(f"  R²:   {test_r2:.4f}")
print("=" * 80)

# Step 10: Save model
print("\n[10/10] Saving model to disk...")
model_dir = 'model'
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, 'house_price_model.pkl')
scaler_path = os.path.join(model_dir, 'scaler.pkl')
features_path = os.path.join(model_dir, 'feature_names.pkl')

joblib.dump(model, model_path)
joblib.dump(scaler, scaler_path)
joblib.dump(X_train_encoded.columns.tolist(), features_path)

print(f"✓ Model saved to: {model_path}")
print(f"✓ Scaler saved to: {scaler_path}")
print(f"✓ Feature names saved to: {features_path}")

# Verify model reloading
print("\n[BONUS] Verifying model reloading...")
loaded_model = joblib.load(model_path)
loaded_scaler = joblib.load(scaler_path)
loaded_features = joblib.load(features_path)

sample_pred_orig = model.predict(X_test_scaled[:5])
sample_pred_loaded = loaded_model.predict(loaded_scaler.transform(X_test_encoded[:5]))

if np.allclose(sample_pred_orig, sample_pred_loaded):
    print("✓ Model reloaded successfully! Predictions match perfectly!")
else:
    print("⚠ Warning: Predictions differ slightly")

print("\n" + "=" * 80)
print("✓ TRAINING COMPLETE!")
print("=" * 80)
print("\nNext steps:")
print("1. Run the Flask app: python app.py")
print("2. Open http://localhost:5000 in your browser")
print("3. Test house price predictions")
print("\nAll model files are saved in the 'model/' directory")
print("=" * 80)
