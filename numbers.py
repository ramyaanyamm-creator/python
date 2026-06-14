import re

n = int(input())

for _ in range(n):
    mobile = input()

    if re.match(r'^[789]\d{9}$', mobile):
        print("YES")
    else:
        print("NO")