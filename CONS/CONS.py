import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import fasta_reader
szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_gc (4).txt')
n=len(DNS)
d["A"]=0
d["C"]=0
d["T"]=0
d["G"]=0
di["A"]=[]
di["C"]=[]
di["T"]=[]
di["G"]=[]
for i in range(len(DNS[0])):
    for j in range(n):
        d[DNS[j][i]]==d[DNS[j][i]]+1