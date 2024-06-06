FROM python:3.8

WORKDIR /app

RUN pip install scikit-learn joblib flask

COPY ml-model/isolation_forest_model.pkl .

COPY dockerfile/predict.py .

CMD ["python", "predict.py"]
