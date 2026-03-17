# AI Churn Whisperer — Personalized Retention

Hi — I’m **Moumita**. This little app is my hand-on project that predicts whether a telco customer will churn and gives one-line, practical retention suggestions you can actually use (for example: “Offer 1-month free streaming + 10% discount for 2 months”).

I built it to show that ML should not be a black box: predictions must be explainable, actionable and tied to business decisions.

---

## Live demo
**Not deployed yet.**  
To run on your machine (quick & local):

```powershell
cd /c/Kaggale/"Churn whishper"
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python download_models.py
python -m streamlit run app.py
# then open http://localhost:8501 in your browser