from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    data = input().split()
    name = " ".join(data[:-1])
    price = int(data[-1])

    if name in items:
        items[name] += price
    else:
        items[name] = price

for name, price in items.items():
    print(name, price)
