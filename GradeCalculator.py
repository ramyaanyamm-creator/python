# Student Grade Calculator

name = input("Enter student name: ")
marks = []

for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("\n--- Result ---")
print("Student:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)