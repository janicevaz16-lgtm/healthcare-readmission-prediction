# Healthcare Readmission Prediction

## Project Overview

This project explores the use of healthcare data analytics and machine
learning to understand and predict hospital readmission within 30 days
among patients with diabetes.

The project follows a structured data science workflow:

1. Project planning
2. Data cleaning and preprocessing
3. Exploratory data analysis
4. Predictive modelling
5. Model evaluation
6. Healthcare interpretation

## Dataset

The project uses the Diabetes 130-US Hospitals for Years 1999–2008
dataset from the UCI Machine Learning Repository.

The dataset contains 101,766 hospital encounters and 47 features.

## Project Objective

The objective is to investigate whether historical encounter,
demographic, medication, procedure and healthcare-utilisation variables
can help identify encounters associated with 30-day readmission.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Analysis

The project includes:

- Data quality assessment
- Missing-value analysis
- Outlier investigation
- Feature engineering
- Exploratory data analysis
- Correlation analysis
- Data visualization
- Logistic Regression
- Random Forest
- Gradient Boosting
- Confusion matrix
- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC
- Calibration
- Threshold analysis

## Important Finding

In the reference dataset, 11,357 of 101,766 encounters are classified
as readmitted within 30 days, representing approximately 11.16%.

This class imbalance demonstrates why accuracy alone should not be used
to evaluate the predictive model.

## Healthcare Considerations

The project treats machine-learning predictions as decision-support
information rather than clinical decisions.

Potential limitations include:

- Historical data
- Class imbalance
- Data leakage
- Missing information
- Hospital-specific practices
- Demographic subgroup differences
- Model drift

Any real-world deployment would require clinical validation,
governance, privacy protection and human oversight.

## Repository Structure

```text
docs/       Project reports
notebooks/  Python analysis notebooks
src/        Python scripts
figures/    Visualizations
data/       Dataset documentation
