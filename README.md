# Customer-Churn-Prediction-Logistic-Regression

•Built a predictive model for customer churn using the Telco Customer Churn Dataset for 7000+ customers which contained 21 features covering customer demographics, services subscribed, account details, and payment methods

•Identified key indicators of churn:
	•High monthly charges, short tenure, and the presence of paperless billing increased churn likelihood.
	•Long-term contracts, phone service availability, and additional services like tech support and online security decreased churn.

•Trained multiple machine learning models (Logistic Regression, Random Forest, and Gradient Boosting) and selected the best based on a balance of accuracy and recall.

•Evaluated models using precision, recall, F1-score, and confusion matrices, balancing the trade-offs between accuracy and recall for better churn prediction.

•Visualized feature importance for logistic regression, highlighting tenure as the most significant negative predictor and monthly charges as the highest positive contributor to churn.
 
•Deployed the final logistic regression model as a REST API using Flask, enabling real-time churn predictions.
