# src/__init__.py

import pandas as pd
import os

def load_data():
    """Load diabetes dataset from the fixed CSV file path."""

    file_path = os.path.normpath("C:/Users/KIIT/Downloads/diabetes.csv")

    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Read the CSV file
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}")
        return data

    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")
