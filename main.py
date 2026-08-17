import pandas as pd


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"{file_path} loaded successfully.")
        return data

    except FileNotFoundError:
        print(f"Error: {file_path} was not found.")
        return None



def check_data(students, courses):
    print("\nStudents info:")
    students.info()

    print("\nCourses info:")
    courses.info()

    print("\nMissing values in Students:")
    print(students.isna().sum())

    print("\nMissing values in Courses:")
    print(courses.isna().sum())

    print("\nDuplicate student_id in Students:")
    print(students["student_id"].duplicated().sum())

    print("\nDuplicate student_id in Courses:")
    print(courses["student_id"].duplicated().sum())


def clean_key(df, key):
    df = df.copy()

    df[key] = df[key].astype(str)
    df[key] = df[key].str.strip()
    print(f"Unique values in '{key}': {df[key].nunique()}")

    return df

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


def clean_text_column(df, column, use_title=False):
    df = df.copy()

    df[column] = df[column].str.strip()
    if use_title:
        df[column] = df[column].str.title()

    return df



students = load_data("students.csv")
courses = load_data("courses.csv")

students = clean_text_column(students, "name", use_title=True)
students = clean_text_column(students, "city", use_title=True)
courses = clean_text_column(courses, "course")

if students is not None and courses is not None:

    students = clean_key(students, "student_id")
    courses = clean_key(courses, "student_id")
    
    
    check_data(students, courses)

    merged = merge_data(
        students,
        courses,
        "student_id"
    )

    if merged is not None:
        print("\nMerged data:")
        print(merged)

else:
    print("Program stopped because one or more files could not be loaded.")