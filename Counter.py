from collections import Counter

input()                         # Number of shoes (not needed)

shoes = list(map(int, input().split()))

stock = Counter(shoes)

customers = int(input())

money = 0

for i in range(customers):
    size, price = map(int, input().split())

    if stock[size] > 0:
        money += price
        stock[size] -= 1

print(money)
