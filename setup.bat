@echo off
REM House Price Prediction System - Setup Script (Windows)
REM This script will set up the environment and run the Flask app

echo ===============================================
echo House Price Prediction System - Setup
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Checking Python installation...
python --version
echo.

REM Create virtual environment
echo [2/4] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)
echo.

REM Activate virtual environment
echo [3/4] Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
echo.

REM Display next steps
echo [4/4] Setup complete!
echo.
echo ===============================================
echo NEXT STEPS:
echo ===============================================
echo.
echo 1. Open model_building.ipynb in Jupyter Notebook
echo    Command: jupyter notebook model/model_building.ipynb
echo.
echo 2. Run all cells in the notebook to train the model
echo    This will create:
echo    - model/house_price_model.pkl
echo    - model/scaler.pkl
echo    - model/feature_names.pkl
echo.
echo 3. Run the Flask app:
echo    Command: python app.py
echo.
echo 4. Open http://localhost:5000 in your browser
echo.
echo 5. Test predictions and verify the app works
echo.
echo 6. Deploy to Render.com, PythonAnywhere, or Streamlit Cloud
echo    See DEPLOYMENT_GUIDE.md for detailed instructions
echo.
echo ===============================================
echo.

REM Ask if user wants to start Jupyter
set /p start_jupyter="Do you want to start Jupyter Notebook now? (y/n): "
if /i "%start_jupyter%"=="y" (
    jupyter notebook model/model_building.ipynb
) else (
    echo Setup complete. You can now run the notebook manually.
    echo To activate virtual environment later, use: venv\Scripts\activate.bat
    pause
)
