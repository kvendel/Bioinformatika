import requests
with open(r'C:\Users\kvend\Downloads\rosalind_mprt.txt') as f:
    lines = f.readlines()
ID=[]
for i in range(len(lines)):
    ID.append(lines[i][:-1])
for i in ID:
    s="http://www.uniprot.org/uniprot/"+i
    resp=requests.get(s)
    print(resp.text)
