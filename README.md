MLOps Production Pipeline with FastAPI:
This is a simple end-to-end machine learning production pipeline project. 
The goal of this project is to show how a machine learning model can be:
Trained
Saved
Monitored
Served using FastAPI
Connected with a basic HTML frontend
Managed using Git

It’s a beginner-friendly structure to understand how ML moves from notebook to production.
Project Structure
mlops-production-pipeline/

│
├── app/
│   ├── main.py            # FastAPI application
│   ├── model_loader.py    # Loads saved model and makes predictions
│   ├── templates/
│   │   └── index.html     # Simple HTML frontend
│   └── __init__.py
│
├── src/
│   ├── train.py           # Model training script
│   ├── validate.py        # Data validation checks
│   └── monitor.py         # Model performance monitoring
│
├── models/                # Saved models
├── logs/                  # Training logs
│
├── requirements.txt
├── .gitignore
└── README.md

What This Project Does
1️⃣ Data Validation
Before training, the dataset is checked for:
Missing values
Schema mismatch
This helps prevent training errors.

2️⃣ Model Training
A simple Logistic Regression model is trained.
Data is split into train and test sets.
Accuracy is calculated.
Model is saved in the models/ folder.
Accuracy is logged in logs/metrics_log.txt.

3️⃣ Monitoring
The monitor.py script:
Reads previous accuracy
Compares it with the latest one
Alerts if performance drops significantly
This simulates basic production monitoring.

4️⃣ FastAPI Application
The FastAPI app:
Loads the saved model
Takes user input (age, salary, experience)
Returns prediction
Displays result on a simple HTML page

How To Run This Project
Step 1: Create Virtual Environment
python -m venv venv

Activate it:
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

Step 2: Install Requirements
pip install -r requirements.txt

Step 3: Train the Model
cd src
python train.py

This will:
Train the model
Save it inside models/
Log accuracy inside logs/
Step 4: (Optional) Run Monitoring
python monitor.py

Step 5: Start FastAPI Server
Go back to project root and run:
uvicorn app.main:app --reload

Open in browser:
http://127.0.0.1:8000

You’ll see a simple form where you can enter values and get predictions.

Why This Project Is Useful:
This project demonstrates:
Basic MLOps workflow
Model saving and loading
Logging and monitoring
API deployment
Frontend integration
Clean project structure
It’s a good starting point before moving to:
MLflow

Author:
Built as a hands-on MLOps practice project to understand how ML systems work in production.