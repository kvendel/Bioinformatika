import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import codon

f = open(r'C:\Users\kvend\Downloads\rosalind_prot.txt')
s=str(f.read())
c=""
for i in range(len(s)-1):
    if i%3==0:
        c=c+codon(s[i:i+3])
print(c)