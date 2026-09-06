Healthcare Readmission Prediction

🚀 What did I build?
An end-to-end healthcare analytics and machine-learning project predicting hospital encounters associated with readmission within 30 days among patients with diabetes.

📊 What data did I use?
UCI Diabetes 130-US Hospitals dataset — 101,766 encounters, 47 features, 130 hospitals, 1999–2008.

🔎 What did I discover?
11,357 encounters (11.16%) were readmitted within 30 days. Prior inpatient utilization was the strongest permutation-importance feature.

🤖 Which model performed better?
Random Forest achieved 72.06% accuracy, 27.47% F1, 0.6671 ROC-AUC and 0.2124 PR-AUC, outperforming Logistic Regression on most selected metrics. Logistic Regression had higher recall: 51.92% vs 47.42%.

📓 Where can I see the notebooks?
notebooks/01_data_cleaning.ipynb
notebooks/02_eda_visualization.ipynb
notebooks/03_predictive_modeling.ipynb
