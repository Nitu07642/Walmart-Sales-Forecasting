import streamlit as st
import joblib
import pandas as pd

# 1. Saved Model load
model = joblib.load('walmart_sales_rf_model.pkl')

st.title("🚀 Walmart Future Sales Predictor AI")
st.write("Enter details below to predict weekly sales.")

# 2. input to user
col1, col2 = st.columns(2)

with col1:
    store = st.number_input("Store Number", min_value=1, max_value=45, value=1)
    dept = st.number_input("Department Number", min_value=1, max_value=99, value=1)
    size = st.number_input("Store Size", value=150000)
    store_type = st.selectbox("Store Type", options=[0, 1, 2], format_func=lambda x: ["Type A", "Type B", "Type C"][x])

with col2:
    is_holiday = st.selectbox("Is it a Holiday?", options=[0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    month = st.slider("Month", 1, 12, 1)
    week = st.slider("Week of Year", 1, 52, 1)
    year = st.selectbox("Year", [2012, 2013, 2014])

# 3. Prediction Button
if st.button("Predict Sales"):
    # Input to DataFrame 
    input_data = pd.DataFrame([[store, dept, size, store_type, is_holiday, month, week, year]], 
                              columns=['Store', 'Dept', 'Size', 'Type', 'IsHoliday', 'Month', 'Week', 'Year'])
    
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Weekly Sales: ${prediction[0]:,.2f}")