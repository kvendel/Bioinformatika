import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import fasta_reader, DNAcodon

szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_splc.txt')
DNA=DNS[0]
subs=DNS[1:]
for t in subs:
    out=[]
    for i in range(len(DNA)-len(t)):
        if DNA[i:i+len(t)]==t:
            out.append(i)
    for i in out:
        DNA=DNA[:i]+DNA[i+len(t):len(DNA)]
c=""
for i in range(len(DNA)):
    if i%3==0:
        c=c+DNAcodon(DNA[i:i+3])
print(c[:-1])