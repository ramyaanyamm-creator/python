students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = list(map(int, input("Enter 3 marks: ").split()))

        average = sum(marks) / len(marks)

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "Fail"

        students[name] = [marks, average, grade]

    elif choice == "2":
        for name, data in students.items():
            print(name, data)

    elif choice == "3":
        break