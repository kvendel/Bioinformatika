with open(r'C:\Users\kvend\Downloads\rosalind_dbru.txt') as f:
    lines = f.readlines()
mers=[]
for i in range(len(lines)):
    mers.append(lines[i][:-1])
edges=set()
for m in mers:
    edges.add((m[:-1],m[1:]))
    rm=""
    for i in range(len(m)):
        if m[i]=="A":
            rm=rm+"T"
        if m[i]=="T":
            rm=rm+"A"
        if m[i]=="G":
            rm=rm+"C"
        if m[i]=="C":
            rm=rm+"G"
    rm=rm[::-1]
    edges.add((rm[:-1],rm[1:]))
for e in edges:
    print("("+e[0]+", "+e[1]+")")