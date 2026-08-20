import logging

def check_data(students, courses):
    logging.info("Checking Students DataFrame.")
    students.info()

    logging.info("Checking Courses DataFrame.")
    courses.info()

    logging.info(
        f"Missing values in Students:\n{students.isna().sum()}"
    )

    logging.info(
        f"Missing values in Courses:\n{courses.isna().sum()}"
    )

    logging.info(
        "Duplicate student_id in Students: "
        f"{students['student_id'].duplicated().sum()}"
    )

    logging.info(
        "Duplicate student_id in Courses: "
        f"{courses['student_id'].duplicated().sum()}"
    )