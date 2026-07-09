def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"


name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for Subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)

print("\n----- Student Report -----")
print("Name:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)