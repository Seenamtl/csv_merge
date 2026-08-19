import pandas as pd


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"{file_path} loaded successfully.")
        return data

    except FileNotFoundError:
        print(f"Error: {file_path} was not found.")
        return None