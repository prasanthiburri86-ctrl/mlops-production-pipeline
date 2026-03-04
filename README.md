# MLOps Production Pipeline with FastAPI

This is a simple end-to-end machine learning production pipeline project.

The goal of this project is to demonstrate how a machine learning model can be:

- **Trained**
- **Saved**
- **Monitored**
- **Served using FastAPI**
- **Connected with a basic HTML frontend**
- **Managed using Git**

It is designed as a beginner-friendly structure to understand how a machine learning model moves from a notebook environment into a production-ready system.

---

# What This Project Does

## 1️⃣ Data Validation

Before training, the dataset is checked for:

- Missing values  
- Schema mismatch  

This helps prevent training errors and ensures clean input data.

---

## 2️⃣ Model Training

- A simple **Logistic Regression** model is trained.  
- Data is split into training and testing sets.  
- Accuracy is calculated.  
- The model is saved in the `models/` folder.  
- Accuracy is logged in `logs/metrics_log.txt`.  

---

## 3️⃣ Monitoring

The `monitor.py` script:

- Reads the previous accuracy  
- Compares it with the latest accuracy  
- Alerts if performance drops significantly  

This simulates basic production monitoring.

---

## 4️⃣ FastAPI Application

The FastAPI app:

- Loads the saved model  
- Takes user input (`age`, `salary`, `experience`)  
- Returns prediction  
- Displays the result on a simple HTML page  

---

# How To Run This Project

## Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

## Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

---

## Step 3: Train the Model

```bash
cd src
python train.py
```

This will:

- Train the model  
- Save it inside `models/`  
- Log accuracy inside `logs/`  

---

## Step 4: (Optional) Run Monitoring

```bash
python monitor.py
```

---

## Step 5: Start FastAPI Server

Go back to the project root and run:

```bash
uvicorn app.main:app --reload
```

Open in your browser:

```
http://127.0.0.1:8000
```

You will see a simple form where you can enter values and get predictions.

---

# Why This Project Is Useful

This project demonstrates:

- Basic MLOps workflow  
- Model saving and loading  
- Logging and monitoring  
- API deployment  
- Frontend integration  
- Clean project structure  

It is a good starting point before moving to more advanced tools such as:

- MLflow  
- Docker  
- CI/CD pipelines  
- Cloud deployment  

---

# Author

Built as a hands-on MLOps practice project to understand how machine learning systems work in production.