import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load your structured dataset (replace with your actual data)
# Assume 'X' contains features (CPU, memory, disk metrics) & 'y' contains labels (0 for normal, 1 for anomaly)
# X = ...
# y = ...

# Split data into training & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = IsolationForest(contamination=0.05, random_state=42)  

# Train the model
clf.fit(X_train_scaled)

# Save the model to a file
model_filename = 'isolation_forest_model.pkl' #adjust the path accordingly
joblib.dump(clf, model_filename)


