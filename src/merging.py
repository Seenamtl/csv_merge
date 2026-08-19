import pandas as pd


def check_merge_key(left_df, right_df, key):
    left_duplicates = left_df[key].duplicated().sum()
    right_duplicates = right_df[key].duplicated().sum()

    print(f"Duplicates in left DataFrame: {left_duplicates}")
    print(f"Duplicates in right DataFrame: {right_duplicates}")

    if left_duplicates == 0 and right_duplicates == 0:
        relationship = "one_to_one"

    elif left_duplicates == 0 and right_duplicates > 0:
        relationship = "one_to_many"

    elif left_duplicates > 0 and right_duplicates == 0:
        relationship = "many_to_one"

    else:
        relationship = "many_to_many"

    print(f"Relationship: {relationship}")

    return relationship

def merge_data(left_df, right_df, key, how="outer"):

    valid_merge_types = ["inner", "left", "right", "outer"]

    if key not in left_df.columns:
        print(f"Error: '{key}' does not exist in the left DataFrame.")
        return None

    if key not in right_df.columns:
        print(f"Error: '{key}' does not exist in the right DataFrame.")
        return None

    if how not in valid_merge_types:
        print(f"Error: '{how}' is not a valid merge type.")
        return None

    relationship = check_merge_key(
        left_df,
        right_df,
        key
    )
    if relationship == "many_to_many":
        print("Warning: many-to-many relationship detected.")
        print("Merge stopped to prevent unexpected row multiplication.")
        return None

    merged = pd.merge(
        left_df,
        right_df,
        on=key,
        how=how,
        indicator=True,
        validate=relationship
    )

    print(f"Rows in left DataFrame: {len(left_df)}")
    print(f"Rows in right DataFrame: {len(right_df)}")
    print(f"Rows after merge: {len(merged)}")

    return merged
