import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import datetime

from validate import validate_data

# Create synthetic dataset
np.random.seed(42)

data = pd.DataFrame({
    "age": np.random.randint(20, 60, 200),
    "salary": np.random.randint(20000, 100000, 200),
    "experience": np.random.randint(1, 20, 200)
})

data["purchased"] = (
    (data["salary"] > 50000) &
    (data["experience"] > 5)
).astype(int)

validate_data(data)

X = data[["age", "salary", "experience"]]
y = data["purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Create folders if not exist
os.makedirs("./models", exist_ok=True)
os.makedirs("./logs", exist_ok=True)

# Save model
model_path = "./models/model_latest.pkl"
joblib.dump(model, model_path)

# Log metrics
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
with open("./logs/metrics_log.txt", "a") as f:
    f.write(f"{timestamp} - Accuracy: {accuracy}\n")

print("Model saved successfully!")