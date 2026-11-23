def armstrong(n):
    temp = n
    total = 0
    power = len(str(n))

    while n > 0:
        digit = n % 10
        total = total + digit ** power
        n = n // 10

    if temp == total:
        print("Armstrong Number")
    else:
        print("Not Armstrong")

armstrong(153)
