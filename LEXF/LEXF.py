with open(r'C:\Users\kvend\Downloads\rosalind_lexf.txt') as f:
    lines = f.readlines()
s=lines[0][:-1].split()
m=len(s)
n=int(lines[1][:-1])
def adding(s,a):
    return(s+a)
def printer(n,s,t):
    for i in range(n):
        t=t+s[i]
        printer(n-1,s,t)
        if i==n-1:
            print(t)
print(s,n)
printer(n,s,"")
