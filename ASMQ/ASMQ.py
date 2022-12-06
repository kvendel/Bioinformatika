with open(r'C:\Users\kvend\Downloads\rosalind_asmq.txt') as f:
    lines = f.readlines()
contigs=[]
for i in range(len(lines)):
    contigs.append(lines[i][:-1])
n=len(contigs)
s=0
for i in range(n):
    s=s+len(contigs[i])

def NXX(XX,c,n,s):
    L=0
    t=0
    for i in range(n):
        if len(c[i])>=L:
            t=t+len(c[i])
    while(t>s*XX/100):
        L=L+1
        t=0
        for i in range(n):
            if len(c[i]) >= L:
                t = t + len(c[i])
    return(L-1)
out50=NXX(50,contigs,n,s)
out75=NXX(75,contigs,n,s)
print(out50,out75)