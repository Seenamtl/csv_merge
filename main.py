import logging
from pathlib import Path

from src.loading import load_data
from src.cleaning import (
    clean_key,
    clean_text_column,
    clean_numeric_column,
    handle_missing
)
from src.merging import merge_data
from src.validation import check_data

from config import (
    STUDENTS_FILE,
    COURSES_FILE,
    MERGE_KEY,
    MERGE_TYPE,
    AGE_MISSING_METHOD
)

from src.saving import save_data

BASE_DIR = Path(__file__).resolve().parent

RAW_DIR = BASE_DIR / "data" / "raw"
CLEANED_DIR = BASE_DIR / "data" / "cleaned"
OUTPUT_DIR = BASE_DIR / "data" / "output"
LOG_DIR = BASE_DIR / "logs"

CLEANED_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(
            LOG_DIR / "pipeline.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)





def main():
    logging.info("Data pipeline started.")

    students = load_data(RAW_DIR / STUDENTS_FILE)
    courses = load_data(RAW_DIR / COURSES_FILE)

    if students is None or courses is None:
        logging.error(
            "Program stopped because one or more files could not be loaded."
        )
        return

    students = clean_key(students, MERGE_KEY)
    courses = clean_key(courses, MERGE_KEY) 

    students = clean_text_column(
        students,
        "name",
        use_title=True
    )

    students = clean_text_column(
        students,
        "city",
        use_title=True
    )

    courses = clean_text_column(
        courses,
        "course"
    )

    students = clean_numeric_column(
        students,
        "age"
    )

    courses = clean_numeric_column(
        courses,
        "grade"
    )

    students = handle_missing(
    students,
    "age",
    method=AGE_MISSING_METHOD

    )

    check_data(
        students,
        courses
    )

    save_data(
    students,
    CLEANED_DIR / "cleaned_students.csv"

    )

    save_data(
    courses,
    CLEANED_DIR / "cleaned_courses.csv"
    )

    merged = merge_data(
    students,
    courses,
    MERGE_KEY,
    how=MERGE_TYPE

    )

    if merged is None:
        logging.error("Merge failed.")
        return

    logging.info("Merge completed successfully.")

    print(merged)

    save_data(
    merged,
    OUTPUT_DIR / "merged_output.csv"
    )

    logging.info("Data pipeline finished successfully.")


if __name__ == "__main__":
    main()