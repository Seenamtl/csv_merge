import pandas as pd
from pathlib import Path

from src.loading import load_data
from src.cleaning import (
    clean_key,
    clean_text_column,
    clean_numeric_column,
    handle_missing
)
from src.merging import merge_data




BASE_DIR = Path(__file__).resolve().parent

RAW_DIR = BASE_DIR / "data" / "raw"
CLEANED_DIR = BASE_DIR / "data" / "cleaned"
OUTPUT_DIR = BASE_DIR / "data" / "output"

CLEANED_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)





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






students = load_data(RAW_DIR / "students.csv")
courses = load_data(RAW_DIR / "courses.csv")

if students is not None and courses is not None:

    students = clean_key(students, "student_id")
    courses = clean_key(courses, "student_id")

    students = clean_text_column(students, "name", use_title=True)
    students = clean_text_column(students, "city", use_title=True)
    courses = clean_text_column(courses, "course")

    students = clean_numeric_column(students, "age")
    courses = clean_numeric_column(courses, "grade")

    students = handle_missing(
        students,
        "age",
        method="median"
    )

    check_data(students, courses)

    students.to_csv(
        CLEANED_DIR / "cleaned_students.csv",
        index=False
    )

    courses.to_csv(
        CLEANED_DIR / "cleaned_courses.csv",
        index=False
    )

    merged = merge_data(
        students,
        courses,
        "student_id"
    )

    if merged is not None:
        print("\nMerged data:")
        print(merged)

        merged.to_csv(
            OUTPUT_DIR / "merged_output.csv",
            index=False
        )

else:
    print("Program stopped because one or more files could not be loaded.")