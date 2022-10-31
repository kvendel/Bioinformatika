import math
with open(r'C:\Users\kvend\Downloads\rosalind_prob.txt') as f:
    lines = f.readlines()
DNS=lines[0][:-1]
p=lines[1].split()
n=len(DNS)
m=len(p)
out=[]
for i in range(m):
    logp=0
    for j in range(n):
        if DNS[j]=="C" or DNS[j]=="G":
            logp=logp+math.log(float(p[i])/2,10)
        else:
            logp = logp + math.log((1-float(p[i]))/2,10)
    out.append(logp)
print(*out)