# OpsAI
A fusion of “Ops” (for SRE/DevOps practices) and “AI” (for machine learning). 
### Real-Time Anomaly Detection Project 

### Overview
Combining SRE practices with machine learning that can lead to powerful insights and improved system reliability. This project focuses on real-time anomaly detection using machine learning and Kubernetes(GKE).

#### 1. Data Preparation and Model Training:
- Follow the instructions mentioned here for data collection and structuring [Additional Information](Data-collection-and-structuring.md).
- Train an **Isolation Forest** model for anomaly detection based on the dataset created following the instructions above. [1](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)
- Save the trained model as ```isolation_forest_model.pkl``` [ML Model](ml-model).

#### 2. Containerization and Deployment:
- Create a Docker image for our model [Docker file](dockerfile/Dockerfile).
- The ```predict.py``` file in your Docker container contains the logic to load the trained Isolation Forest model (isolation_forest_model.pkl) and make predictions.
- Additionally, set up a GitHub trigger in Cloud Build to automatically build the image using the Dockerfile from the repository.
- Then push the image to Google Container Registry (GCR) using ```cloudbuild.yaml```.

#### 3. Kubernetes Cluster Setup:
- Provision a GKE cluster within a custom VPC network using Terraform and cloudbuild. [2](https://developer.hashicorp.com/terraform/tutorials/kubernetes/gke)
- Use the ```deploy-infra.yaml``` file to deploy the Terraform code in order to provision the infrastructure using GCP Cloud Build.
- Now, deploy the containerized model to Kubernetes using ```deployment.yaml``` file.
  ```
  kubeclt apply -f deployment.yaml
  ```
### Next Steps
Now that we have the foundation in place, here’s what’s next:
#### 1. Inference and Monitoring:
- Set up an inference pipeline to feed real-time data to your model. [3](https://towardsdatascience.com/machine-learning-with-docker-and-kubernetes-batch-inference-4a25328f23c7)
- Monitor the model’s performance using Prometheus or other observability tools.
- Implement alerts for anomalies or degradation.

#### 2. Testing and Validation:
- Use live application or metric data to validate the model’s predictions. [4](https://www.analyticsvidhya.com/blog/2019/08/11-important-model-evaluation-error-metrics)
- Compare model predictions with actual outcomes.
- Iterate and improve the model as needed.
