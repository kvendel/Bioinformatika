import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import fasta_reader
szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_gc (4).txt')
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