import streamlit as st
import pandas as pd
import joblib

# Load saved model and preprocessor
@st.cache_resource
def load_model():
    xgb = joblib.load('xgb_model.pkl')
    preprocessor = joblib.load('preprocessor.pkl')
    return xgb, preprocessor

st.title("🚀 AI Churn Whisperer – Personalized Retention")
xgb, preprocessor = load_model()

st.header("Enter Customer Details")
tenure = st.slider("Tenure (months)", 0, 72, 10)
monthly_charges = st.number_input("Monthly Charges ($)", 18.0, 120.0, 70.0)
contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
senior = st.selectbox("Senior Citizen?", ['NO', 'YES'])
internet = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
payment = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

if st.button("Predict Risk & Get Retention Tip"):
    input_data = pd.DataFrame({
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [tenure * monthly_charges],
        'Contract': [contract],
        'SeniorCitizen': [senior],
        'InternetService': [internet],
        'PaymentMethod': [payment],
        'gender': ['Male'],
        'Partner': ['No'],
        'Dependents': ['No'],
        'PhoneService': ['Yes'],
        'MultipleLines': ['No'],
        'OnlineSecurity': ['No'],
        'OnlineBackup': ['No'],
        'DeviceProtection': ['No'],
        'TechSupport': ['No'],
        'StreamingTV': ['No'],
        'StreamingMovies': ['No'],
        'PaperlessBilling': ['Yes']
    })

    input_pre = preprocessor.transform(input_data)
    prob = xgb.predict_proba(input_pre)[0, 1]
    
    st.metric("Churn Probability", f"{prob:.1%}", delta="High 🚨" if prob > 0.40 else "Low 😊")
    
    if prob > 0.40:
        st.success("**Retention Whisper:** Offer 20% discount for 2 months + free tech support call. Email: 'We value you – stay with us!'")
    else:
        st.info("**Retention Whisper:** Excellent customer! Suggest adding Streaming TV pack for loyalty bonus.")