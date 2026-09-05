# Healthcare Readmission Prediction
# Data Cleaning and Preprocessing
# Author: Janice Vaz

import pandas as pd
import numpy as np


def load_data(file_path):
    """
    Load the diabetes hospital readmission dataset.
    """
    df = pd.read_csv(file_path)
    return df


def inspect_data(df):
    """
    Display basic information about the dataset.
    """
    print("Dataset shape:", df.shape)

    print("\nFirst five records:")
    print(df.head())

    print("\nColumn information:")
    print(df.info())

    print("\nMissing values:")
    print(df.isnull().sum().sort_values(ascending=False))


def replace_missing_symbols(df):
    """
    Convert '?' values used in the original dataset
    into proper missing-value markers.
    """
    df = df.replace("?", np.nan)
    return df


def remove_duplicate_records(df):
    """
    Remove completely duplicated records.
    """
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print("Records before removing duplicates:", before)
    print("Records after removing duplicates:", after)
    print("Duplicates removed:", before - after)

    return df


if __name__ == "__main__":

    print("Healthcare Readmission Prediction")
    print("---------------------------------")

    # Replace this path with the location of your dataset
    file_path = "data/diabetic_data.csv"

    # Load dataset
    df = load_data(file_path)

    # Initial inspection
    inspect_data(df)

    # Replace '?' with NaN
    df = replace_missing_symbols(df)

    # Remove duplicate records
    df = remove_duplicate_records(df)

    print("\nData cleaning step completed.")
