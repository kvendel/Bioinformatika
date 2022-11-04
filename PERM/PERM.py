from itertools import permutations
import math
with open(r'C:\Users\kvend\Downloads\rosalind_perm.txt') as f:
    lines = f.readlines()
n=int(lines[0][:-1])
print(math.factorial(n))
l = list(permutations(range(1, n+1)))
for i in l:
    print(*i)