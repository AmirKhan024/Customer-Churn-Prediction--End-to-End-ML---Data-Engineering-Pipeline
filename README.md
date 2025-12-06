# 🚀 Customer Churn Prediction - End-to-End ML Pipeline with Web Application & Data Engineering

[![AWS](https://img.shields.io/badge/AWS-Lambda%20%7C%20S3%20%7C%20EC2-orange)](https://aws.amazon.com/)
[![Apache Airflow](https://img.shields.io/badge/Apache-Airflow-017CEE?logo=apache-airflow)](https://airflow.apache.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-29B5E8)](https://www.snowflake.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)](https://flask.palletsprojects.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)](https://powerbi.microsoft.com/)

---

## 🎯 Project Overview

A **comprehensive customer churn prediction solution** that combines machine learning, cloud-based data engineering, and web application development. This end-to-end system features an **event-driven ETL pipeline**, **automated ML training**, a **user-facing Flask web application**, and **interactive Power BI dashboards** to help telecommunications companies proactively identify at-risk customers and improve retention strategies.

### 🌐 Live Web Application
The predictive model is deployed as a web application accessible at:
**[https://amirkhan024.pythonanywhere.com/](https://amirkhan024.pythonanywhere.com/)**

Users can input customer features (tenure, contract type, service usage, payment methods, charges) and receive real-time churn predictions with confidence percentages.

---

## 💼 Business Problem & Solution

### The Challenge
Customer churn is a critical issue for telecom companies, resulting in significant revenue loss and reduced customer lifetime value. Organizations struggle with:
- 📉 Identifying which customers are likely to leave
- 🔍 Understanding the key factors driving churn
- ⏰ Detecting churn signals early enough to intervene
- 📊 Translating data insights into actionable retention strategies

### Our Solution
This project delivers a **complete AI-powered churn management system** that:
- ✅ **Predicts churn** with 92.43% accuracy using Random Forest ML models
- ✅ **Automates the entire pipeline** from data ingestion to model deployment
- ✅ **Provides real-time predictions** through an intuitive web interface
- ✅ **Delivers actionable insights** via interactive Power BI dashboards
- ✅ **Scales effortlessly** with event-driven serverless architecture
- ✅ **Handles class imbalance** using advanced SMOTEENN techniques

---

## 🔄 Pipeline Workflow

### End-to-End Flow (Automated)

1. **Upload CSV** → S3 raw bucket
2. **Lambda 1 triggers** → Data transformation (1-2 min)
3. **Output to 2 paths**:
   - `ml/` folder → **Lambda 2 triggers** → ML training (1 min)
   - `snowflake/` folder → **Snowpipe triggers** → Data warehouse load (2-3 min)
4. **Airflow monitors** → 5-task DAG validates pipeline
5. **Flask app** → Real-time predictions from latest model
6. **Power BI** → Dashboards refresh from Snowflake

---

## 🏆 Key Achievements

- **92.43% Model Accuracy** - Random Forest classifier with optimized hyperparameters
- **Real-time Processing** - Event-driven architecture with AWS Lambda (sub-minute latency)
- **Production Web App** - Flask application deployed on PythonAnywhere
- **Automated Pipeline** - Zero manual intervention after initial setup
- **Scalable Design** - Handles increasing data volumes seamlessly
- **Class Imbalance Handling** - SMOTEENN for balanced training data
- **Interactive Dashboards** - Comprehensive Power BI visualizations
- **Production Ready** - Monitoring, logging, error handling, and model versioning


### 2. Power BI Dashboard

![churn_telecom_first](https://github.com/user-attachments/assets/8dfedac0-80a2-4336-803a-8274f35b0087)

![churn_telecom_second](https://github.com/user-attachments/assets/40c12dd1-d69e-4b00-84e4-e9cf45432e59)

### 3. System Architecture

**Hybrid Event-Driven + Orchestrated Architecture**:
1. **Data Ingestion**: S3-triggered Lambda for automated ETL
2. **Processing**: Event-driven transformations with feature engineering
3. **ML Training**: Automated model training with versioning
4. **Orchestration**: Apache Airflow for workflow monitoring
5. **Data Warehouse**: Snowflake with Snowpipe for real-time loading
6. **Web Application**: Flask for user-facing predictions
7. **Analytics**: Power BI dashboards for business intelligence

---

## 🛠️ Technology Stack

### Cloud & Infrastructure
- **AWS S3**: Data lake storage
- **AWS Lambda**: Serverless compute for ETL and ML
- **AWS EC2**: Airflow orchestration server
- **AWS CloudWatch**: Logging and monitoring
- **PythonAnywhere**: Flask app hosting

### Data Processing & ML
- **Python 3.12**: Primary language
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations
- **Scikit-learn**: ML (Random Forest, SMOTEENN)
- **Joblib**: Model serialization

### Web & Orchestration
- **Flask**: Web framework
- **Apache Airflow**: Workflow orchestration
- **Boto3**: AWS SDK

### Analytics
- **Snowflake**: Cloud data warehouse
- **Snowpipe**: Continuous data ingestion
- **Power BI**: Interactive visualizations

---

## ✨ Key Features

### 🔄 Automated ETL Pipeline
- Event-driven architecture (S3 triggers)
- Data cleaning and transformation
- Feature engineering (TenureGroup, ChargeRatio)
- Dual output: encoded (ML) and decoded (analytics)

### 🤖 Machine Learning
- **Algorithm**: Random Forest (100 trees, depth 10)
- **Accuracy**: 92.43%
- **Class Balancing**: SMOTEENN technique
- **Feature Importance**: Contract (16.43%), Tenure (15.31%), TotalCharges (9.29%)
- **Model Versioning**: Timestamped artifacts in S3

### 🌐 Flask Web Application
- Real-time churn predictions
- User-friendly interface
- **Live Demo**: [amirkhan024.pythonanywhere.com](https://amirkhan024.pythonanywhere.com/)
- Confidence percentage output

### 📊 Power BI Dashboards
- 9 comprehensive visualizations
- Customer segmentation (High/Medium/Low risk)
- Financial impact analysis
- Real-time data from Snowflake

---

## 🚀 Quick Start Guide

### Prerequisites
- AWS Account (S3, Lambda, EC2 permissions)
- Snowflake Account
- Python 3.11+
- Power BI Desktop
- PythonAnywhere Account (for deployment)

### Step 1: AWS Setup

```bash
# Create S3 buckets
aws s3 mb s3://first-customer-churn-raw
aws s3 mb s3://second-customer-churn-transformed
aws s3 mb s3://third-customer-churn-ml-model

# Deploy Lambda functions (see full setup for code)
# Lambda 1: Data transformation
# Lambda 2: ML model training
```

### Step 2: Airflow on EC2

```bash
# Launch t2.medium EC2 instance
# Install Airflow
python3 -m venv airflow_venv
source airflow_venv/bin/activate
pip install apache-airflow boto3 pandas scikit-learn

# Deploy DAG
cp customer_churn_etl_dag.py ~/airflow/dags/
airflow standalone
```

### Step 3: Snowflake Configuration

```sql
-- Create database and schemas
CREATE DATABASE telecom_churn_db;
CREATE SCHEMA churn_schema;

-- Create tables and Snowpipe
CREATE TABLE churn_transformed_encoded (...);
CREATE PIPE churn_pipe AUTO_INGEST = TRUE AS
COPY INTO churn_transformed_encoded FROM @s3_stage;
```

### Step 4: Flask Deployment

```bash
# Local testing
pip install flask pandas scikit-learn joblib
python app.py

# Deploy to PythonAnywhere
# Upload files, configure virtualenv, set WSGI config
```

### Step 5: Power BI

1. Connect to Snowflake view (`vw_churn_decoded`)
2. Create 9 visualizations (see dashboard images)
3. Schedule refresh (daily)


### Model Development Process
1. **EDA**: Identified class imbalance (26.5% churn)
2. **Preprocessing**: Feature engineering, encoding
3. **Balancing**: SMOTEENN for minority class
4. **Training**: Random Forest with hyperparameter tuning
5. **Deployment**: Joblib serialization, S3 storage


## 📈 Business Insights

### Key Findings
- **Contract Type**: Month-to-month = 42% churn, 2-year = 3% churn
- **Tenure**: First year = 50% churn, 4+ years = 7% churn
- **Internet Service**: Fiber optic = 41% churn (quality concerns)
- **Payment Method**: Electronic check = 45% churn (auto-pay users = 15%)

### Customer Segmentation
- 🔴 **High Risk** (26.5%): Month-to-month + <1yr tenure
- 🟡 **Medium Risk** (17%): 1-2yr tenure + Fiber optic
- 🟢 **Low Risk** (56.5%): 2yr contract + 4+ yr tenure

### Recommendations
1. Offer contract upgrade incentives
2. Implement first-year engagement programs
3. Improve fiber optic service quality
4. Push auto-payment enrollment
5. Promote add-on services (TechSupport reduces churn 15%)

---

## 🔮 Future Enhancements

### Technical
- [ ] Real-time streaming with Kinesis
- [ ] Automated monthly model retraining
- [ ] SHAP values for explainability
- [ ] Docker containerization
- [ ] CI/CD with GitHub Actions

### ML
- [ ] Test XGBoost, LightGBM
- [ ] Hyperparameter tuning with Optuna
- [ ] Customer Lifetime Value prediction
- [ ] Churn probability scores (0-100)
- [ ] Next-best-action recommendations

### Analytics
- [ ] Real-time alerting for high-risk customers
- [ ] Customer journey analysis
- [ ] Cohort retention tracking
- [ ] What-if scenario modeling

---

## 🛡️ Monitoring

### AWS CloudWatch
- Lambda logs: Invocation count, duration, errors
- Retention: 7 days
- Custom metrics for pipeline health

### Airflow Dashboard
- UI: `http://ec2-ip:8080`
- DAG run history
- Task-level logs
- Email alerts on failure

### Snowflake
- Snowpipe history tracking
- Query performance monitoring
- Data quality checks


