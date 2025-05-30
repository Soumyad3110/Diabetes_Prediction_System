# src/data_loader.ipynb

import pandas as pd

def load_data(filepath):
    """
    Loads a CSV file into a DataFrame.
    """
    print(f"Loading data from {filepath}")
    return pd.read_csv(filepath)
