import pandas as pd
import logging



def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info(f"{file_path} loaded successfully.")
        return data

    except FileNotFoundError:
        logging.error(f"{file_path} was not found.")
        return None