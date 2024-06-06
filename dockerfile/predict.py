import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_model(model_filename):
    return joblib.load(model_filename)

def predict_anomalies(model, input_data):
    predictions = model.predict(input_data)
    return (predictions == -1).astype(int)  
  
# Initialize the model
model_filename = "isolation_forest_model.pkl"
loaded_model = load_model(model_filename)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = np.array(data['features'])  # Assuming 'features' is an array of metrics
        anomaly_predictions = predict_anomalies(loaded_model, input_data)
        return jsonify({'predictions': anomaly_predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
