def student_details(*args, **kwargs):
    print("Subjects:")
    for subject in args:
        print(subject)

    print("\nStudent Information:")
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(
    "Python",
    "Machine Learning",
    "Data Science",
    name="Ramya",
    age=19,
    branch="AIML"
)