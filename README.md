# 🚀 Walmart Advanced Sales Forecasting & Automation Pipeline

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest%20%7C%20XGBoost-orange.svg)](https://scikit-learn.org/)
[![Automation](https://img.shields.io/badge/Automation-n8n-red.svg)](https://n8n.io/)

## 📌 Project Overview
Predicting demand is a critical challenge in the retail industry. This project provides an end-to-end solution for **Walmart Store Sales Forecasting**, helping businesses optimize their inventory and supply chain. 

Unlike traditional analysis, this project features a **real-time automation pipeline** .

---

<img width="814" height="258" alt="image" src="https://github.com/user-attachments/assets/a6ccbc26-c392-40f7-881b-d439eb5844be" />


---

## 🚀 Key Features
 **Time-Series Forecasting:** Built using Random Forest and XGBoost to capture complex seasonal patterns and holiday spikes.
 **Intelligent Automation:** Integrated with **n8n** for automated data ingestion and processing.
 **Web Deployment:** A user-friendly **Streamlit** dashboard for real-time sales prediction and visualization.
 **Scalable Architecture:** Designed to handle large datasets efficiently.

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
Seasonal Trends: High sales spikes observed during February, June, and the peak holiday season in December.

<img width="1635" height="771" alt="image" src="https://github.com/user-attachments/assets/cf7d1ab9-684f-4c36-8f0a-42f4482debcf" />


<img width="1644" height="776" alt="image" src="https://github.com/user-attachments/assets/8585f5f8-cc50-4d4d-8902-c32c2a03167d" />
<img width="1422" height="162" alt="image" src="https://github.com/user-attachments/assets/13d1597f-253f-4184-a83e-049a51582ea4" />

<img width="1550" height="679" alt="image" src="https://github.com/user-attachments/assets/ffee59eb-e1bd-4079-b150-ec011eb8b009" />

<img width="1122" height="668" alt="image" src="https://github.com/user-attachments/assets/199a240f-84cf-4157-a720-d7558e138a62" />



---

## 📁 Project Structure
```text
├── data/                   # Dataset files (ignored in git)
├── notebooks/              # EDA and Model Training
├── app.py                  # Streamlit Web App Code
├── .gitignore              # Files to exclude (Model/Data)
└── README.md               # Project Documentation
