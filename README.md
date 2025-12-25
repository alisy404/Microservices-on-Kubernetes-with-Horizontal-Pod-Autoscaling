# Python Microservice on Kubernetes with Horizontal Pod Autoscaling

This project demonstrates a **containerized Python microservice** deployed on **Kubernetes** with **automatic scaling** using the **Horizontal Pod Autoscaler (HPA)** based on CPU utilization.

The application is built using **FastAPI**, packaged with **Docker**, deployed on a **Minikube Kubernetes cluster**, exposed using a **NodePort Service**, and scaled automatically when CPU load increases.

---

## What This Project Does

- Runs a Python FastAPI application inside Docker containers
- Deploys the containerized application to Kubernetes
- Exposes the application externally using a NodePort Service
- Collects CPU metrics using Kubernetes Metrics Server
- Automatically scales pods up and down using HPA
- Simulates CPU load to demonstrate real autoscaling behavior

---

## Tools and Technologies Used

- Python (FastAPI)
- Docker
- Kubernetes
- Minikube
- Metrics Server
- Horizontal Pod Autoscaler (HPA)
- kubectl
- curl

---

## Project Structure

python-app/
├── app/
│ ├── main.py
│ └── requirements.txt
├── Dockerfile
├── k8s/
│ ├── deployment.yaml
│ ├── service.yaml
│ └── hpa.yaml
└── README.md


---

## Requirements (Install Before Running)

### System
- Ubuntu 22.04 / 24.04 / 25.10
- Docker installed and running
- Internet access for image pulls

### Tools
- Docker
- kubectl
- Minikube

Verify installations:
```bash
docker --version
kubectl version --client
minikube version

How to Run the Project
Step 1: Start Kubernetes Cluster
minikube start


Enable metrics server:

minikube addons enable metrics-server


Verify metrics:

kubectl top nodes

Step 2: Build and Push Docker Image
docker build -t <dockerhub-username>/python-k8s-api:v1 .
docker push <dockerhub-username>/python-k8s-api:v1

Step 3: Deploy Application to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml


Check status:

kubectl get all

Step 4: Access the Application

Get Minikube IP:

minikube ip


Access the service:

curl http://<MINIKUBE-IP>:30007/

API Endpoints and Output
Root Endpoint /
curl http://<MINIKUBE-IP>:30007/


Response:

{
  "message": "Python Microservice Running on Kubernetes"
}

Load Endpoint /load
curl http://<MINIKUBE-IP>:30007/load


Response:

{
  "status": "CPU load generated"
}


This endpoint generates CPU load to trigger Kubernetes autoscaling.

Verify Autoscaling

Monitor pod scaling:
kubectl get pods -w

Monitor HPA:
kubectl get hpa -w


Expected behavior:
  Pod replicas increase automatically when CPU usage rises
  Pods scale down when load decreases

Final Outcome:
  Python application runs successfully inside Kubernetes
  Service is reachable from outside the cluster
  Metrics Server provides CPU metrics
  Horizontal Pod Autoscaler dynamically scales pods based on load


---------------------------------------------------------------------------------------------------
Thankyou# Microservices-on-Kubernetes-with-Horizontal-Pod-Autoscaling
