import numpy as np
with open(r'C:\Users\kvend\Downloads\rosalind_seto.txt') as f:
    lines = f.readlines()
n=int(lines[0][:-1])
As=lines[1][1:-2].split(", ")
Bs=lines[2][1:-2].split(", ")
A=set()
B=set()
for e in As:
    A.add(int(e))
for e in Bs:
    B.add(int(e))
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
alap=set(np.arange(1,n+1))
print(alap.difference(A))
print(alap.difference(B))
