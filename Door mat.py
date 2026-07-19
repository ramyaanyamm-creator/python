# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

# Top Half
for i in range(1, n, 2):
    pattern = ".|." * i
    print(pattern.center(m, "-"))

# Middle
print("WELCOME".center(m, "-"))

# Bottom Half
for i in range(n - 2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(m, "-"))
