import logging

import pandas as pd


def check_merge_key(left_df, right_df, key):
    left_duplicates = left_df[key].duplicated().sum()
    right_duplicates = right_df[key].duplicated().sum()

    logging.info(
        f"Duplicates in left DataFrame: {left_duplicates}"
    )
    logging.info(
        f"Duplicates in right DataFrame: {right_duplicates}"
    )

    if left_duplicates == 0 and right_duplicates == 0:
        relationship = "one_to_one"

    elif left_duplicates == 0 and right_duplicates > 0:
        relationship = "one_to_many"

    elif left_duplicates > 0 and right_duplicates == 0:
        relationship = "many_to_one"

    else:
        relationship = "many_to_many"

    logging.info(
        f"Merge relationship detected: {relationship}"
    )

    return relationship

def merge_data(left_df, right_df, key, how="outer"):

    valid_merge_types = ["inner", "left", "right", "outer"]

    if key not in left_df.columns:
        logging.error(
            f"'{key}' does not exist in the left DataFrame."
        )
        return None

    if key not in right_df.columns:
        logging.error(
            f"'{key}' does not exist in the right DataFrame."
        )
        return None

    if how not in valid_merge_types:
        logging.error(
            f"'{how}' is not a valid merge type. "
            f"Choose from: {valid_merge_types}"
        )
        return None

    relationship = check_merge_key(
        left_df,
        right_df,
        key
    )

    if relationship == "many_to_many":
        logging.warning(
            "Many-to-many relationship detected."
        )
        logging.warning(
            "Merge stopped to prevent unexpected row multiplication."
        )
        return None

    merged = pd.merge(
        left_df,
        right_df,
        on=key,
        how=how,
        indicator=True,
        validate=relationship
    )

    logging.info(
        f"Merge completed: {len(left_df)} left rows, "
        f"{len(right_df)} right rows, "
        f"{len(merged)} output rows."
    )

    return merged
