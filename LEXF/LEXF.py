with open(r'C:\Users\kvend\Downloads\rosalind_lexf.txt') as f:
    lines = f.readlines()
s=lines[0][:-1].split()
m=len(s)
n=int(lines[1][:-1])
def printer(n,m,s,t):
    if n==0:
        print(t)
        return
    for i in range(m):
        t=t+s[i]
        printer(n-1,m,s,t)
        t=t[:-1]
printer(n,m,s,"")