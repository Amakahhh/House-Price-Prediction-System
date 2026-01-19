# DEPLOYMENT GUIDE - House Price Prediction System

## Quick Deployment Checklist

- [ ] Model trained and saved (run model_building.ipynb)
- [ ] All dependencies installed
- [ ] App tested locally (http://localhost:5000)
- [ ] Code pushed to GitHub
- [ ] Environment variables configured
- [ ] Deployment platform account created
- [ ] Live URL added to submission file

---

## OPTION 1: RENDER.COM (RECOMMENDED ⭐)

### Step 1: Prepare Your Repository

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit: House Price Prediction System"

# Create .gitignore
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".env" >> .gitignore
```

### Step 2: Create render.yaml

Create a file named `render.yaml` in the root directory:

```yaml
services:
  - type: web
    name: house-price-prediction
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.10.0
```

### Step 3: Deploy

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Set these settings:
   - **Name**: house-price-prediction
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click "Create Web Service"
7. Wait for deployment (2-5 minutes)
8. Your app will be live at: `https://house-price-prediction-xxx.onrender.com`

---

## OPTION 2: PYTHONANYWHERE.COM

### Step 1: Upload Code

1. Go to https://www.pythonanywhere.com
2. Sign up (free account)
3. Dashboard → Files → Upload files from your project
4. Upload all files maintaining the structure

### Step 2: Create Virtual Environment

1. Dashboard → Consoles → New console → Bash
2. Run these commands:

```bash
cd ~/mysite  # or your project folder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Configure Web App

1. Dashboard → Web → Add a new web app
2. Choose Python 3.10 (or latest available)
3. Choose Flask
4. In WSGI configuration file, modify it to:

```python
import sys
path = '/home/{username}/mysite'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

5. Click "Reload" web app
6. Your app will be live at: `https://{username}.pythonanywhere.com`

---

## OPTION 3: STREAMLIT CLOUD

### Step 1: Restructure App (Optional)

Create `streamlit_app.py`:

```python
import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# Load model
model = joblib.load('model/house_price_model.pkl')
scaler = joblib.load('model/scaler.pkl')
features = joblib.load('model/feature_names.pkl')

st.title("🏠 House Price Prediction System")

col1, col2 = st.columns(2)

with col1:
    quality = st.slider("Overall Quality", 1, 10, 5)
    living_area = st.number_input("Living Area (sq ft)", 100, 10000, 1500)
    basement = st.number_input("Basement Area (sq ft)", 0, 10000, 1000)

with col2:
    garage = st.number_input("Garage Size (cars)", 0, 10, 2)
    year = st.number_input("Year Built", 1800, 2024, 2000)
    neighborhood = st.selectbox("Neighborhood", 
        ['Ames', 'Edwards', 'BriarDale', 'OldTown', 'Sawyer', 
         'NoRidge', 'NridgHt', 'SomerSet', 'CollgCr'])

if st.button("Predict Price"):
    # Create input data and predict
    st.success(f"Predicted Price: ${prediction:,.2f}")
```

### Step 2: Deploy

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Click "New app"
4. Connect GitHub repository
5. Select main branch and `streamlit_app.py` as main file
6. Click "Deploy"

---

## OPTION 4: VERCEL (Advanced)

### Requires API conversion to serverless functions
This is more complex. Only choose if you have serverless experience.

---

## TESTING BEFORE DEPLOYMENT

### Local Testing

```bash
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the app
python app.py

# Test in browser
# Go to http://localhost:5000
```

### Test the Prediction API

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "OverallQual": 7,
    "GrLivArea": 1500,
    "TotalBsmtSF": 1000,
    "GarageCars": 2,
    "YearBuilt": 2000,
    "Neighborhood": "Ames"
  }'
```

---

## TROUBLESHOOTING

### Issue: Model files not found after deployment

**Solution**: Make sure the model files are committed to GitHub:
```bash
git add model/*.pkl
git commit -m "Add trained model files"
git push
```

### Issue: Module not found error

**Solution**: Ensure all dependencies are in requirements.txt:
```bash
pip freeze > requirements.txt
```

### Issue: Port already in use

**Solution**: Use different port:
```bash
python app.py --port 5001
```

### Issue: App crashes after deployment

**Solution**: Check logs on deployment platform:
- Render: Logs tab
- PythonAnywhere: Web app error log
- Streamlit Cloud: View logs

---

## SUBMISSION TEMPLATE

After deployment, fill in this information:

```
Name: [Your Full Name]
Matric Number: [Your Matric Number]
Machine Learning Algorithm Used: Random Forest Regressor
Model Persistence Method: Joblib
Live URL: https://[your-deployed-app-url]
GitHub Repository: https://github.com/[username]/HousePrice_Project_YourName_MatricNo
```

Save as `HousePrice_hosted_webGUI_link.txt` and submit to Scorac by **January 22, 2026, 11:59 PM**

---

## FINAL CHECKLIST FOR SCORAC SUBMISSION

- [ ] Name and Matric Number filled correctly
- [ ] Machine Learning Algorithm documented: Random Forest
- [ ] Model Persistence method: Joblib
- [ ] Live URL is accessible and working
- [ ] GitHub repository link is correct
- [ ] All files uploaded to Scorac in correct structure
- [ ] HousePrice_hosted_webGUI_link.txt included
- [ ] model_building.ipynb included
- [ ] house_price_model.pkl included
- [ ] app.py included
- [ ] requirements.txt included
- [ ] index.html included
- [ ] style.css included

---

**Deadline: Friday, January 22, 2026 - 11:59 PM**

Good luck with your submission! 🚀
