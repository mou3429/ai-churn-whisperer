# AI Churn Whisperer — Personalized Retention

Hi — I’m **Moumita**.This project demonstrates an end-to-end machine learning workflow for predicting telecom customer churn and generating practical retention strategies. 

I built a small interactive Streamlit app where you can enter customer details and instantly see the predicted churn risk along with a simple, actionable retention suggestion — for example: “Offer 1-month free streaming + 10% discount for 2 months”.

I built it to show that ML should not be a black box: predictions must be explainable, actionable and tied to business decisions.

---

## Live Demo

A deployed version of the application is available here:

**Interactive App:**  
https://your-app-name.streamlit.app

This small web interface allows you to simulate real customer profiles and see how the churn prediction model behaves in different scenarios. The goal is to demonstrate how a machine learning model can be turned into a practical decision-support tool for customer retention teams.

### What the Demo Shows

The application takes basic customer account details as input and immediately returns three things:

1. **Predicted Churn Probability**

Example output:

Churn Probability: **18.1%**  
Status: **Low Risk**

2. **Suggested Retention Action**

Instead of just predicting churn, the system proposes a simple action that a retention team could take.

Example:

Retention Whisper:  
*Excellent customer. Suggest offering a Streaming TV pack as a loyalty bonus.*

3. **Feature Contribution Explanation**

The app also visualizes the most influential factors that affected the prediction for that specific customer.  
For example, the explanation may show that:

- longer **tenure** significantly decreases churn risk  
- certain **contract types** improve customer retention  
- higher **monthly charges** may slightly increase churn probability

This makes the prediction transparent and easier to interpret from a business perspective.

### How to Run the Application Locally

If you want to run the project locally:

```bash
python -m streamlit run app.py