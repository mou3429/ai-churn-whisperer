# 🚀 AI Churn Whisperer — Personalized Retention

[![Streamlit](https://img.shields.io/badge/Streamlit-deploy-orange)](PUT_STREAMLIT_LINK_HERE)  
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**One-line:** Streamlit app that predicts customer churn (XGBoost) and provides per-customer retention actions with SHAP explainability. Models are hosted externally and downloaded at runtime so the repository stays lightweight and production-ready.

---

## 🔗 Live demo
**Open this link:** PUT_STREAMLIT_LINK_HERE  
*(If not deployed yet, run locally: `python -m streamlit run app.py` after installing requirements.)*

---

## Why this project stands out (what makes it Top-1%)
- **Production-aware**: model artifacts are not committed to Git — `download_models.py` fetches them at runtime.  
- **Explainable & actionable**: integrated SHAP explanations to translate predictions into concrete retention actions for marketing/ops.  
- **Business-first**: includes simple ROI and A/B test planning so decisions can be executed and measured.  
- **Reproducible**: `requirements.txt`, CI (GitHub Actions), and a Dockerfile (optional) are included to recreate the environment.

---

## Repo structure (root folder)