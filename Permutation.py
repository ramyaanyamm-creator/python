# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, r = input().split()

for i in permutations(sorted(s), int(r)):
    print(''.join(i))
