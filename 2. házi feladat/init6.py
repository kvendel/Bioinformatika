with open(r'C:\Users\kvend\Downloads\rosalind_ini6.txt') as f:
    lines = f.readlines()
s=""
for i in range(len(lines)):
        s=s+str(lines[i][0:-1])
t=s.split()
d={}
for word in t:
    if word not in d.keys():
        d[word]=1
    else:
        d[word]=d[word]+1
for w in d.items():
    print(w[0], w[1])