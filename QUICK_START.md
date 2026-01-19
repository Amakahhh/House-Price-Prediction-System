# 🚀 QUICK START GUIDE

## Your House Price Prediction System is Ready!

This guide will get your project up and running in minutes.

---

## ✅ What's Already Done

- ✓ Complete Jupyter notebook for model development
- ✓ Flask web application
- ✓ Responsive HTML/CSS interface
- ✓ All dependencies configured
- ✓ Deployment guides included

---

## 📋 Next Steps (In Order)

### STEP 1️⃣: Install Dependencies (5 minutes)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### STEP 2️⃣: Train the Model (10-15 minutes)

**Install Jupyter:**
```bash
pip install jupyter
```

**Run the notebook:**
```bash
jupyter notebook model/model_building.ipynb
```

**In the notebook:**
- Execute all cells from top to bottom
- The notebook will download the dataset automatically
- Model files will be saved to the `model/` directory
- You'll see evaluation metrics (MAE, RMSE, R²)

**Files created after running notebook:**
- `model/house_price_model.pkl` - Trained model
- `model/scaler.pkl` - Feature scaler
- `model/feature_names.pkl` - Feature column names

### STEP 3️⃣: Test Locally (5 minutes)

```bash
python app.py
```

**Open in browser:** `http://localhost:5000`

**Test the form:**
1. Fill in house details
2. Click "Predict Price"
3. See the predicted price

**All working?** ✅ Ready for deployment!

### STEP 4️⃣: Deploy (Varies by platform)

Choose ONE of these options:

#### **OPTION A: Render.com (EASIEST - 10 minutes)**

1. Push code to GitHub (create a new repository)
2. Go to https://render.com
3. Sign up with GitHub
4. Click "New Web Service"
5. Select your repository
6. Build command: `pip install -r requirements.txt`
7. Start command: `gunicorn app:app`
8. Click "Create"
9. Wait for deployment (2-5 minutes)
10. Share the generated URL!

**Your live app:** `https://house-price-prediction-xxx.onrender.com`

#### **OPTION B: PythonAnywhere (10 minutes)**

1. Sign up at pythonanywhere.com
2. Upload your project files
3. Create a Python virtual environment
4. Configure Flask web app
5. Reload the app
6. Your live URL will be `https://yourusername.pythonanywhere.com`

#### **OPTION C: Streamlit Cloud (5 minutes)**

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Click "New app"
4. Select your repository and `streamlit_app.py`
5. Click "Deploy"

See **DEPLOYMENT_GUIDE.md** for detailed instructions for each platform.

### STEP 5️⃣: Fill Submission Info

Edit `HousePrice_hosted_webGUI_link.txt`:

```
Name: [Your Full Name]
Matric Number: [Your Matric Number]
Machine Learning Algorithm Used: Random Forest Regressor
Model Persistence Method: Joblib
Live URL: [Your deployed URL]
GitHub Repository: [Your GitHub link]
```

### STEP 6️⃣: Submit to Scorac

**Deadline: Friday, January 22, 2026 - 11:59 PM**

Upload to Scorac with this structure:
```
/HousePrice_Project_YourName_MatricNo/
├── app.py
├── requirements.txt
├── HousePrice_hosted_webGUI_link.txt
├── model/
│   ├── model_building.ipynb
│   └── house_price_model.pkl
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
**Solution:** Install requirements
```bash
pip install -r requirements.txt
```

### "No such file or directory: model/house_price_model.pkl"
**Solution:** Run the Jupyter notebook first to train the model

### "Port 5000 already in use"
**Solution:** Use different port
```bash
python app.py --port 5001
```

### "RuntimeError: Working outside of request context"
**Solution:** Make sure you're running Flask app (python app.py), not just opening HTML

### Jupyter notebook won't open
**Solution:** Install and use Jupyter
```bash
pip install jupyter
jupyter notebook
```

---

## 📊 What the Model Does

**Input:**
- Overall Quality (1-10)
- Living Area (square feet)
- Basement Area (square feet)
- Garage Size (number of cars)
- Year Built
- Neighborhood

**Output:**
- Predicted house price

**Algorithm:** Random Forest Regressor (100 trees)
**Accuracy:** ~75-80% R² score (typical for this dataset)

---

## 🎯 Project Requirements Met

✅ **PART A - Model Development**
- [x] Load dataset
- [x] Handle missing values
- [x] Feature selection (6 of 9 features)
- [x] Categorical encoding
- [x] Feature scaling
- [x] Random Forest implementation
- [x] Model training
- [x] Evaluation metrics (MAE, MSE, RMSE, R²)
- [x] Model saved with Joblib
- [x] Model reloading verified

✅ **PART B - Web GUI**
- [x] Flask application
- [x] HTML/CSS interface
- [x] Load saved model
- [x] User input form
- [x] Display predictions

✅ **PART C - GitHub**
- [x] Correct file structure
- [x] All required files

✅ **PART D - Deployment**
- [x] Deployment guides for 4 platforms

✅ **Scorac Submission**
- [x] README.md
- [x] DEPLOYMENT_GUIDE.md
- [x] HousePrice_hosted_webGUI_link.txt (template)

---

## 📚 Important Files

| File | Purpose |
|------|---------|
| `model_building.ipynb` | Trains the ML model |
| `app.py` | Flask web server |
| `templates/index.html` | Web interface |
| `static/style.css` | Styling |
| `requirements.txt` | Dependencies |
| `README.md` | Full documentation |
| `DEPLOYMENT_GUIDE.md` | Platform-specific deployment |
| `HousePrice_hosted_webGUI_link.txt` | Submission template |

---

## ⏰ Timeline

- **Today**: Steps 1-3 (setup, train, test locally)
- **Tomorrow**: Step 4 (deploy to cloud)
- **Before Jan 22**: Steps 5-6 (finalize and submit)

---

## 🆘 Need Help?

1. **Check DEPLOYMENT_GUIDE.md** for platform-specific issues
2. **Check README.md** for full documentation
3. **Verify notebook ran** - Check model/ directory for .pkl files
4. **Test locally first** - Before deploying

---

## ✨ Final Tips

- Test locally thoroughly before deploying
- Deploy early to resolve any platform-specific issues
- Keep your GitHub repository updated
- Double-check Scorac submission format and deadline

---

**You're all set! Happy coding! 🎉**

For any questions, refer to the detailed documentation in:
- README.md
- DEPLOYMENT_GUIDE.md
- Comments in model_building.ipynb
- Flask app documentation in app.py
