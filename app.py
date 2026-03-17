import streamlit as st
import pandas as pd
import joblib

# ---------- Auto-download models (put this just after imports, before loading models) ----------
import os, subprocess, sys

def _download_models_if_missing():
    """
    Ensures two model files exist under ./models/.
    If missing, runs `download_models.py` (which should be in the same folder).
    """
    models_ok = os.path.exists("models/xgb_model.pkl") and os.path.exists("models/preprocessor.pkl")
    if models_ok:
        return True

    # If running inside Streamlit, use streamlit spinner for UX
    try:
        import streamlit as _st  # local import so this code also works when not running streamlit
        spinner = _st.spinner("Model artifacts missing — downloading model files (this may take a minute)...")
        spinner.__enter__()  # start spinner
    except Exception:
        _st = None
        spinner = None

    try:
        # Run the helper script with the same Python interpreter
        print("Model files missing — running download_models.py to fetch them...")
        # Use check_call to raise exception on failure
        subprocess.check_call([sys.executable, "download_models.py"])
    except Exception as e:
        # Clean up spinner and surface a readable error
        if spinner:
            spinner.__exit__(type(e), e, e.__traceback__)
        err_msg = f"Failed to download model artifacts automatically: {e}"
        print(err_msg)
        if _st:
            _st.error("Unable to download model files automatically. Please run `python download_models.py` manually and ensure Drive sharing is 'Anyone with the link'.")
        return False
    else:
        if spinner:
            spinner.__exit__(None, None, None)
        print("Download finished — models should now exist in ./models")
        return os.path.exists("models/xgb_model.pkl") and os.path.exists("models/preprocessor.pkl")

# Call it immediately so later code can load the models
_download_models_if_missing()
# -----------------------------------------------------------------------------------------------

# Load saved model and preprocessor
@st.cache_resource
def load_model():
    """
    Load model and preprocessor from models/ folder.
    This function is cached by Streamlit so the models are loaded only once.
    """
    xgb_path = "models/xgb_model.pkl"
    pre_path = "models/preprocessor.pkl"

    # clear, helpful error message if files missing
    if not (os.path.exists(xgb_path) and os.path.exists(pre_path)):
        raise FileNotFoundError(
            "Model files not found. Please run `python download_models.py` "
            "or check that models exist in the ./models folder."
        )

    xgb = joblib.load(xgb_path)
    preprocessor = joblib.load(pre_path)
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