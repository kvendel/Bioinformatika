with open(r'C:\Users\kvend\Downloads\rosalind_pcov.txt') as f:
    lines = f.readlines()
mers=[]
for i in range(len(lines)):
    mers.append(lines[i][:-1])
# mers=["ATTAC","TACAG","GATTA","ACAGA","CAGAT","TTACA","AGATT"]
m=mers[0]
out=""
for j in range(len(mers)):
    i=0
    while (m[1:]!=mers[i][:-1] or m==mers[i]):
        i=i+1
    out=out+m[0]
    m=mers[i]
print(out)