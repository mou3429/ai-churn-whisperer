# AI Churn Whisperer — Personalized Retention

Hi — I’m **Moumita**. Hi — I’m Moumita. This project demonstrates an end-to-end machine learning workflow for predicting telecom customer churn and generating practical retention strategies. 

I built a small interactive Streamlit app where you can enter customer details and instantly see the predicted churn risk along with a simple, actionable retention suggestion — for example: “Offer 1-month free streaming + 10% discount for 2 months”.

I built it to show that ML should not be a black box: predictions must be explainable, actionable and tied to business decisions.

---

## Live demo
**https://your-app-name.streamlit.app**  
To run on your machine (quick & local):

```powershell
cd /c/Kaggale/"Churn whishper"
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python download_models.py
python -m streamlit run app.py
# then open http://localhost:8501 in your browser