# 📊 AI-Powered Influencer Marketing ROI Prediction System

An end-to-end Machine Learning and Business Analytics project that predicts the **Return on Investment (ROI)** of influencer marketing campaigns using a **Random Forest Regressor**. The application includes an interactive **Streamlit web interface** and **Power BI dashboards** for business insights.

---

## 🚀 Project Overview

This project helps marketing teams estimate the expected ROI of influencer campaigns before launching them. Users enter campaign details through a Streamlit web application, and the trained machine learning model predicts the expected ROI along with a business recommendation.

The project also includes Power BI dashboards for visual analysis of campaign performance and marketing trends.

---

## ✨ Features

- 🤖 AI-based ROI prediction using Machine Learning
- 📊 Interactive Power BI dashboards
- 🌐 User-friendly Streamlit web application
- 📈 Business recommendations based on predicted ROI
- 📋 Campaign summary before prediction
- 🎯 Easy-to-use interface with dropdowns and input fields

---

## 🛠️ Technologies Used

### Programming
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

### Data Visualization
- Power BI

### Machine Learning
- Random Forest Regressor

---

## 📂 Project Structure

```
Influencer_ROI_Project/
│
├── app.py
├── requirements.txt
├── roi_prediction_model.pkl
├── platform_encoder.pkl
├── category_encoder.pkl
├── campaign_encoder.pkl
├── influencer_marketing_roi_dataset.csv
├── dashboard1.png
├── dashboard2.png
├── dashboard3.png
└── README.md
```

---

## 📊 Dataset Features

The model uses the following campaign attributes:

- Platform
- Influencer Category
- Campaign Type
- Engagements
- Estimated Reach
- Campaign Duration
- Spend

Target Variable:

- ROI (Return on Investment)

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Label Encoding
4. Train-Test Split
5. Random Forest Model Training
6. Model Evaluation
7. ROI Prediction
8. Deployment with Streamlit

---

## 📈 Model Performance

Model: **Random Forest Regressor**

Evaluation Metrics:

- R² Score
- Mean Absolute Error (MAE)

The trained model predicts campaign ROI based on campaign characteristics and marketing metrics.

---

## 📊 Dashboard

Power BI dashboards provide insights into:

- ROI Analysis
- Platform Performance
- Campaign Performance
- Spend vs Revenue
- Influencer Category Analysis
- Engagement Trends

---

## 🌐 Streamlit Application

The application includes:

- ROI Prediction Page
- Dashboard Page
- About Page
- Business Recommendations

---

## ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project folder:

```bash
cd YOUR_REPOSITORY
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 👩‍💻 Developed By

**Gopika R**

B.Tech Information Technology

Anna University

---

## 📜 License

This project was developed for educational and internship purposes.
