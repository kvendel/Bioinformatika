with open(r'C:\Users\kvend\Downloads\rosalind_subs.txt') as f:
    lines = f.readlines()
s=lines[0][:-1]
t=lines[1][:-1]
out=[]
for i in range(len(s)-len(t)):
    if s[i:i+len(t)]==t:
        out.append(i+1)
print(*out)