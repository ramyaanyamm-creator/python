import re

n = int(input())

inside_block = False

for _ in range(n):
    line = input()

    if '{' in line:
        inside_block = True

    elif '}' in line:
        inside_block = False

    elif inside_block:
        colors = re.findall(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?', line)

        for color in colors:
            print(color)