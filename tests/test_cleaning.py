import pandas as pd

from src.cleaning import clean_key

from src.merging import merge_data
from src.cleaning import (
    clean_key,
    clean_numeric_column,
    handle_missing,
)



def test_clean_key():
    df = pd.DataFrame({
        "student_id": [" 1001 ", "1002", " 1003"]
    })

    cleaned = clean_key(df, "student_id")

    assert cleaned["student_id"].tolist() == [
        "1001",
        "1002",
        "1003"
    ]
    
    




def test_many_to_many_merge_is_stopped():
    left_df = pd.DataFrame({
        "student_id": ["1001", "1001", "1002"],
        "name": ["Ali", "Ali", "Sara"]
    })

    right_df = pd.DataFrame({
        "student_id": ["1001", "1001", "1003"],
        "course": ["Python", "AI", "Data Science"]
    })

    result = merge_data(
        left_df,
        right_df,
        "student_id"
    )

    assert result is None


def test_one_to_many_merge_works():
    left_df = pd.DataFrame({
        "student_id": ["1001", "1002"],
        "name": ["Ali", "Sara"]
    })

    right_df = pd.DataFrame({
        "student_id": ["1001", "1001", "1002"],
        "course": ["Python", "AI", "Data Science"]
    })

    result = merge_data(
        left_df,
        right_df,
        "student_id"
    )

    assert result is not None
    assert len(result) == 3
    
    ali_courses = result[
    result["student_id"] == "1001"
    ]["course"].tolist()   

    assert ali_courses == ["Python", "AI"]
    
    
    
def test_clean_numeric_column():
    df = pd.DataFrame({
        "age": ["23", "25", "unknown", "21"]
    })

    cleaned = clean_numeric_column(
        df,
        "age"
    )

    assert cleaned["age"].isna().sum() == 1
    assert cleaned["age"].iloc[0] == 23
    assert cleaned["age"].iloc[1] == 25
    
    

def test_handle_missing_with_median():
    df = pd.DataFrame({
        "age": [21, 23, None, 25, 27]
    })

    cleaned = handle_missing(
        df,
        "age",
        method="median"
    )

    assert cleaned["age"].isna().sum() == 0
    assert cleaned["age"].iloc[2] == 24