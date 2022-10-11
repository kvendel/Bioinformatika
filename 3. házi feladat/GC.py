with open(r'C:\Users\kvend\Downloads\rosalind_gc (4).txt') as f:
    lines = f.readlines()
szam=[]
DNS=[]
for i in range(len(lines)):
    if lines[i][0]==">":
        szam.append(lines[i][:-1])
    else:
        if lines[i-1][0]==">":
            DNS.append(lines[i][:-1])
        else:
            DNS[len(DNS)-1]=DNS[len(DNS)-1]+lines[i][:-1]
optind=0
opt=0
for i in range(len(DNS)):
    s=0
    for j in range(len(DNS[i])):
        if DNS[i][j]=="C" or DNS[i][j]=="G":
            s=s+1
    if s/(len(DNS[i]))>opt:
        optind=i
        opt=s/(len(DNS[i]))
print(szam[optind][1:], "\n",opt*100)