arr = [1,4,6,8,9,10,16]

i = 0
j = len(arr) - 1

target = 15

while i < j:

    current_sum = arr[i] + arr[j]

    if current_sum == target:
        print("Pair found:", arr[i], arr[j])
        break

    elif current_sum > target:
        j -= 1

    else:
        i += 1
