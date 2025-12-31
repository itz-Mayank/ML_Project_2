# Network Security – End-to-End Machine Learning Pipeline

## Project Overview

This project implements a **production-grade, end-to-end Machine Learning pipeline for Network Security**. It follows **industry-level MLOps practices**, starting from data ingestion to model deployment on AWS using Docker and CI/CD.

The main goal is to **detect malicious or anomalous network behavior** using structured data, while ensuring scalability, reproducibility, and automated deployment.

This repository is designed so that **both recruiters and developers** can easily understand:

* How data flows through the system
* How models are trained, evaluated, and versioned
* How deployment is automated using cloud infrastructure

---

## Key Highlights

* Modular ML pipeline (Ingestion → Validation → Transformation → Training → Evaluation → Deployment)
* Schema-based data validation and drift detection
* Feature engineering with KNN Imputation & preprocessing pipelines
* Model selection using accuracy thresholds
* Dockerized deployment on **AWS EC2 + ECR**
* CI/CD automation using **GitHub Actions**

---

## Project Architecture (High-Level)

```
                                                                                                  ┌──────────────┐
                                                                                                  │  Data Source │
                                                                                                  │  (MongoDB)   │
                                                                                                  └──────┬───────┘
                                                                                                         │
                                                                                                         ▼
                                                                                                ┌────────────────────┐
                                                                                                │ Data Ingestion     │
                                                                                                │ - Export from DB   │
                                                                                                │ - Train/Test split │
                                                                                                └────────┬───────────┘
                                                                                                         │
                                                                                                         ▼
                                                                                                ┌────────────────────┐
                                                                                                │ Data Validation    │
                                                                                                │ - Schema check     │
                                                                                                │ - Data drift       │
                                                                                                └────────┬───────────┘
                                                                                                         │
                                                                                                         ▼
                                                                                                ┌────────────────────┐
                                                                                                │ Data Transformation│
                                                                                                │ - Imputation       │
                                                                                                │ - Scaling          │
                                                                                                │ - Feature Engg.    │
                                                                                                └────────┬───────────┘
                                                                                                         │
                                                                                                         ▼
                                                                                                ┌────────────────────┐
                                                                                                │ Model Training     │
                                                                                                │ - Model Factory    │
                                                                                                │ - Best model       │
                                                                                                └────────┬───────────┘
                                                                                                         │
                                                                                                         ▼
                                                                                                ┌────────────────────┐
                                                                                                │ Model Evaluation   │
                                                                                                │ - Accuracy check   │
                                                                                                │ - Model approval   │
                                                                                                └────────┬───────────┘
                                                                                                         │
                                                                                                         ▼
                                                                                                ┌────────────────────┐
                                                                                                │ Deployment         │
                                                                                                │ - Docker           │
                                                                                                │ - AWS ECR / EC2    │
                                                                                                └────────────────────┘
```

---

## Project Structure

```
ML_Project_2/
│
├── networksecurity/
│   ├── components/        # Core pipeline components
│   ├── config/            # Configuration files
│   ├── constant/          # Constant values
│   ├── entity/            # Config & artifact entities
│   ├── exception/         # Custom exception handling
│   ├── logger/            # Logging setup
│   ├── pipeline/          # Training & prediction pipelines
│   ├── utils/             # Utility functions
│
├── artifacts/              # Generated artifacts (versioned)
├── notebooks/              # EDA and experimentation
├── Dockerfile
├── requirements.txt
├── main.py                 # Pipeline trigger
└── README.md
```

---

## Detailed Pipeline Explanation

### 1️. Data Ingestion

* Source: **MongoDB**
* Data exported into a **Feature Store (CSV)**
* Drops unnecessary columns using schema
* Splits data into train and test sets

**Artifacts Generated:**

* Raw CSV
* Train CSV
* Test CSV

---

### 2️. Data Validation

Ensures data consistency before training.

Checks performed:

* Same number of columns
* Correct data types
* Numerical column validation
* **Data drift detection** using statistical distribution comparison

**Artifacts Generated:**

* Validation status
* Drift report

---

### 3️. Data Transformation

Responsible for feature engineering and preprocessing.

Steps:

* KNN Imputation for missing values
* Feature scaling
* Target feature mapping
* Creation of preprocessing pipeline

Final output is converted into **NumPy arrays** for training.

---

### 4️. Model Training

* Uses a **Model Factory** approach
* Trains multiple algorithms
* Evaluates performance on train and test data
* Selects the best model based on expected accuracy

If no model meets the threshold → training fails safely.

**Artifacts Generated:**

* Trained model (`.pkl`)
* Metric report

---

### 5️. Model Evaluation

* Compares newly trained model with the previously deployed model
* Accepts model only if it performs better

Prevents performance regression in production.

---

### 6. Deployment (AWS + Docker)

* Application is containerized using Docker
* Docker image pushed to **AWS ECR**
* Deployed on **AWS EC2**
* CI/CD pipeline using **GitHub Actions**


---

## Tech Stack

* **Language:** Python
* **Database:** MongoDB
* **ML Libraries:** Scikit-learn, Pandas, NumPy
* **MLOps:** Modular pipelines, artifacts, configs
* **Containerization:** Docker
* **Cloud:** AWS EC2, AWS ECR
* **CI/CD:** GitHub Actions

---

## How to Run the Project

```bash
# Clone repository
git clone https://github.com/itz-Mayank/ML_Project_2.git
cd ML_Project_2

# Install dependencies
pip install -r requirements.txt

# Run training pipeline
python main.py
```

---

## Features of this project -

* Real-world **end-to-end ML system**, not just a notebook
* Strong focus on **data validation and drift detection**
* Clean separation of concerns (industry-ready architecture)
* Cloud-native deployment with CI/CD
* Easily extensible to real-time prediction systems

---

## Author

**Mayank Meghwal**
B.Tech Computer Science | Data Science & MLOps Enthusiast

---

⭐ If you like this project, give it a star on GitHub!
