import pandas as pd
import logging



def clean_key(df, key):
    df = df.copy()

    df[key] = df[key].astype(str)
    df[key] = df[key].str.strip()

    logging.info(
        f"Unique values in '{key}': {df[key].nunique()}"
    )

    return df


def clean_text_column(df, column, use_title=False):
    df = df.copy()

    df[column] = df[column].str.strip()
    if use_title:
        df[column] = df[column].str.title()

    return df


def clean_numeric_column(df, column):
    df = df.copy()

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    missing_count = df[column].isna().sum()

    logging.info(
        f"Missing/invalid values in '{column}': {missing_count}"
    )

    return df

def handle_missing(df, column, method="median"):
    df = df.copy()

    if method == "drop":
        df = df.dropna(subset=[column])

    elif method == "mean":
        df[column] = df[column].fillna(
            df[column].mean()
        )

    elif method == "median":
        df[column] = df[column].fillna(
            df[column].median()
        )

    return df