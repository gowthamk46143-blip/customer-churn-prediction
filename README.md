# 📊 Customer Churn Prediction & Analytics

A Machine Learning project that analyzes customer behavior and predicts whether a customer is likely to churn.

## 🚀 Project Overview

Customer churn occurs when a customer stops using a company's service.

This project uses the IBM Telco Customer Churn dataset to analyze customer characteristics, identify churn patterns, and build a Machine Learning model to predict customer churn.

## 🎯 Objectives

- Analyze customer churn patterns
- Perform data cleaning and preprocessing
- Explore customer behavior using data visualization
- Build a Machine Learning classification model
- Evaluate model performance
- Predict customer churn probability
- Create an interactive Streamlit dashboard

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## 🤖 Machine Learning

The project uses **Logistic Regression** for customer churn prediction.

### Model Evaluation

- Accuracy: 79%
- ROC-AUC: 0.83

The model is evaluated using accuracy, precision, recall, F1-score and ROC-AUC.

## 📈 Dashboard Features

The Streamlit dashboard provides:

- Total customer count
- Churned customer count
- Churn rate
- Average monthly charges
- Churn distribution
- Monthly charges analysis
- Customer tenure analysis
- Contract type analysis
- Customer data filtering
- Individual customer churn prediction
- Churn probability

## 📂 Project Structure

```text
customer-churn-prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── app.py
├── data_analysis.py
├── churn_model.pkl
├── .gitignore
└── README.md
