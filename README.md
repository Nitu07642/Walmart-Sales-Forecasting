## 🚀 Walmart Advanced Sales Forecasting 

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest%20%7C%20XGBoost-orange.svg)](https://scikit-learn.org/)

<img width="1261" height="395" alt="image" src="https://github.com/user-attachments/assets/9b24c3e1-e966-4fee-ab8b-77a75d80177a" />

## 📌 Project Overview
Predicting demand is a critical challenge in the retail industry. This project provides an end-to-end solution for **Walmart Store Sales Forecasting**, helping businesses optimize their inventory and supply chain. 

Unlike traditional analysis, this project features a **real-time** .

---

# 🛒 Walmart Strategic Sales Forecasting & BI Dashboard

### 📌 Project Overview
This project demonstrates an end-to-end data pipeline: from **Feature Engineering** and **Machine Learning** in Python to **Strategic Visualization** in an Advanced Excel Dashboard. As a B.Tech graduate aiming for AI Scientist roles, I engineered this to solve retail forecasting challenges.

### 📊 Interactive Dashboard Preview
![Walmart Dashboard Showcase](<img width="1683" height="729" alt="image" src="https://github.com/user-attachments/assets/a3ee677f-82ec-468e-96f8-0f04b5491a48" />
)
*This dashboard features KPI tracking, store-wise slicers, and a unique AI vs. Reality comparison chart.*

---

<img width="1809" height="938" alt="image" src="https://github.com/user-attachments/assets/8c3ffbf0-0a3d-434f-8ec0-f7894b5a0f84" />


---

## 🛠 Technical Stack
| Category | Tools/Technologies |
| :--- | :--- |
| **Language** | Python (Pandas, NumPy, Scikit-Learn) |
| **Algorithms** | Random Forest Regressor, XGBoost |
| **Automation** | n8n, Google Sheets API |
| **Visualization** | Matplotlib, Seaborn, Streamlit |
| **Environment** | Jupyter Notebook, Git, GitHub |

---

## 📊 Performance & Insights
* **Algorithm Choice:** Random Forest was selected for its robustness against non-linear data and departmental variations.
* **Feature Engineering:** Extracted temporal features (Week, Month, Year) and holiday markers which improved accuracy by ~15%.
* **Model Handling:** The final model is highly optimized. (Note: The 2.9GB .pkl model file is excluded via `.gitignore` for repository efficiency but can be provided on request).

---
***Seasonal Trends: High sales spikes observed during February, June, and the peak holiday season in December***.

<img width="1635" height="771" alt="image" src="https://github.com/user-attachments/assets/cf7d1ab9-684f-4c36-8f0a-42f4482debcf" />

***Model Accuracy Visualization: This chart compares the Actual Weekly Sales (Blue) against the Predicted Sales (Orange) for a test sample of 50 data points. The high degree of overlap demonstrates the model's robust ability to capture complex retail trends and seasonal fluctuations with high precision.***

<img width="1640" height="730" alt="image" src="https://github.com/user-attachments/assets/7567040d-b127-4883-a2f5-2db6f4cbe4a9" />


***Model Interpretability - Feature Importance: This chart highlights the key drivers of Walmart's sales. 'Department' and 'Store Size' emerged as the most significant predictors in the Random Forest model. This insight allows stakeholders to focus on high-impact departments to maximize revenue.***


<img width="1643" height="772" alt="image" src="https://github.com/user-attachments/assets/c12740d3-ba56-49db-9433-50ec55e9478e" />
<img width="1643" height="219" alt="image" src="https://github.com/user-attachments/assets/94359d56-3a35-4f5a-86f4-e660f2bd4526" />


***Historical Sales Seasonality: An end-to-end time-series visualization showing weekly sales fluctuations from 2010 to 2012. The massive spikes at the end of each year (Thanksgiving and Christmas) confirm the high impact of holiday seasons on retail demand.***

<img width="1550" height="679" alt="image" src="https://github.com/user-attachments/assets/ffee59eb-e1bd-4079-b150-ec011eb8b009" />

***Business Insight - Holiday Impact: A comparative analysis of average weekly sales during holiday vs. regular weeks. The data clearly shows a significant increase in sales during holiday periods, validating the need for the specialized forecasting system built in this project.***

<img width="1122" height="668" alt="image" src="https://github.com/user-attachments/assets/199a240f-84cf-4157-a720-d7558e138a62" />



---

## 📁 Project Structure
```text
├── data/                   # Dataset files (ignored in git)
├── notebooks/              # EDA and Model Training
├── app.py                  # Streamlit Web App Code
├── .gitignore              # Files to exclude (Model/Data)
└── README.md               # Project Documentation
