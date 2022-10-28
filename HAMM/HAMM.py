with open(r'C:\Users\kvend\Downloads\rosalind_hamm.txt') as f:
    lines = f.readlines()
s=lines[0][:-1]
t=lines[1][:-1]
out=0
for i in range(len(s)):
    if s[i]!=t[i]:
        out=out+1
print(out)