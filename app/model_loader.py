import joblib
import os

MODEL_PATH = os.path.join("models", "model_latest.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def predict(age, salary, experience):
    model = load_model()
    prediction = model.predict([[age, salary, experience]])
    return int(prediction[0])