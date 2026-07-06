# Find the second largest unique number in a list

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("There is no second largest number.")
else:
    unique_numbers.sort(reverse=True)
    print("Second largest number:", unique_numbers[1])