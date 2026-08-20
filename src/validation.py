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