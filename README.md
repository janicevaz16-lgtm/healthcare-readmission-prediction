Healthcare Readmission Prediction

## 🚀 What did I build?
An end-to-end healthcare analytics and machine-learning project predicting hospital encounters associated with readmission within 30 days among patients with diabetes.

## 📊 What data did I use?
UCI Diabetes 130-US Hospitals dataset — 101,766 encounters, 47 features, 130 hospitals, 1999–2008.

## 🔎 What did I discover?
11,357 encounters (11.16%) were readmitted within 30 days. Prior inpatient utilization was the strongest permutation-importance feature.

## 🤖 Which model performed better?
Random Forest achieved 72.06% accuracy, 27.47% F1, 0.6671 ROC-AUC and 0.2124 PR-AUC, outperforming Logistic Regression on most selected metrics. Logistic Regression had higher recall: 51.92% vs 47.42%.

## 📓 Where can I see the notebooks?

- [01 — Data Cleaning & Preprocessing](notebooks/01_data_cleaning.ipynb)
- [02 — EDA & Visualization](notebooks/02_eda_visualization.ipynb)
- [03 — Predictive Modeling](notebooks/03_predictive_modeling.ipynb)

## 📈 Model Evaluation
        The models were evaluated using multiple metrics because the dataset has an imbalanced target, with only 11.16% of encounters readmitted within 30 days.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 67.20% | 17.43% | **51.92%** | 26.10% | 0.6463 | 0.1994 |
| **Random Forest** | **72.06%** | **19.34%** | 47.42% | **27.47%** | **0.6671** | **0.2124** |

### Model Comparison

**Random Forest performed better overall** across accuracy, precision, F1-score, ROC-AUC and PR-AUC.

However, Logistic Regression achieved higher recall:

- Logistic Regression recall: **51.92%**
- Random Forest recall: **47.42%**

This demonstrates an important precision–recall trade-off. In a healthcare screening scenario, a model with higher recall may identify more potentially high-risk encounters, but it may also generate more false-positive alerts.

Therefore, the final model choice should depend on the operational cost of false negatives versus false positives and would require clinical validation before real-world use.

### Random Forest Confusion Matrix

| | Predicted Negative | Predicted Positive |
|---|---:|---:|
| **Actual Negative** | 13,591 | 4,492 |
| **Actual Positive** | 1,194 | 1,077 |

The Random Forest achieved a test-set recall of approximately **47.42%**.

---

## 🏥 Healthcare Considerations

This project is an **educational and portfolio machine-learning project**, not a clinically validated prediction system.

The model demonstrates how historical healthcare data can be analyzed to identify patterns associated with 30-day readmission. However, predictions should be treated as **decision-support information rather than autonomous clinical decisions**.

Important considerations for real-world implementation include:

- **Clinical validation:** Test the model using current and external hospital data.
- **Model calibration:** Ensure predicted probabilities correspond reasonably to observed outcomes.
- **Threshold selection:** Choose prediction thresholds according to clinical and operational priorities.
- **Fairness:** Evaluate performance across demographic groups such as age, gender and race.
- **Privacy:** Protect patient information and follow applicable healthcare data-governance requirements.
- **Model drift:** Monitor performance because patient populations and hospital practices can change over time.
- **Human oversight:** Healthcare professionals should remain responsible for clinical decisions.

---

## ⚠️ Disclaimer

This project is intended for **academic, educational and portfolio purposes only**.

It is **not medical advice**, and the model has not been clinically validated for patient-care decisions.

The predictions should not be used to diagnose, treat, or make autonomous decisions about patients.

---

## 📂 Project Reports

The repository contains the written deliverables for each project stage:

- **Week 1:** Project Planning & Background
- **Week 2:** Data Cleaning & Preprocessing
- **Week 3:** Exploratory Data Analysis & Visualization
- **Week 4:** Predictive Modeling & Algorithm Selection
- **Week 5:** Final Evaluation, Reporting & Recommendations

---

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Google Colab
- Ucimlrepo
