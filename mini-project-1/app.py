import streamlit as st
import pickle
import numpy as np

# Load the trained model
MODEL_PATH ="https://github.com/fdh-123/Meta-Internship/blob/main/mini-project-1/model1.pkl"


try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    st.success("✅ Model loaded successfully!")
except FileNotFoundError:
    st.error("❌ Model file not found. Please check the file path.")

# Define function to predict loan approval
def predict_loan_status(features):
    prediction = model.predict([features])[0]
    return "Approved ✅" if prediction == 1 else "Not Approved ❌"

# Streamlit UI
st.title("🏦 Loan Approval Prediction App")
st.markdown("### Enter Applicant Details Below:")

# Input Fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0, value=5000)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0, value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0, value=100)
loan_amount_term = st.selectbox("Loan Amount Term (in months)", [360, 180, 120, 60])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semi-Urban", "Rural"])

# Convert categorical inputs to numerical values (same as in training)
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
dependents = {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents]
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
property_area = {"Urban": 2, "Semi-Urban": 1, "Rural": 0}[property_area]

# Prepare input for model (excluding Loan_ID)
features = [
    gender, married, dependents, education, self_employed,
    applicant_income, coapplicant_income, loan_amount,
    loan_amount_term, credit_history, property_area
]

# Prediction Button
if st.button("Predict Loan Approval"):
    prediction = predict_loan_status(features)
    st.subheader(f"Result: {prediction}")
