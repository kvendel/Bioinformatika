import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import DNAcodon
from utils import fasta_reader

szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_orf.txt')
s=DNS[0]
orf=[]
for i in range(3):
    j=0
    while(i+j<len(s)):
        if DNAcodon(s[i+j:i+j+3])=="M":
            k=j+3
            prot="M"
            while DNAcodon(s[i+k:i+k+3])!="_" and i+k<len(s):
                prot=prot+DNAcodon(s[i+k:i+k+3])
                k=k+3
            if DNAcodon(s[i+k:i+k+3])=="_":
                orf.append(prot)
        j=j+3
def reverse(s):
    st = ""
    for i in s:
        st = i + st
    return st
s=reverse(s)
t=""
for i in range(len(s)):
    if s[i]=="A":
        t=t+"T"
    if s[i]=="T":
        t=t+"A"
    if s[i]=="G":
        t=t+"C"
    if s[i]=="C":
        t=t+"G"
s=t
for i in range(3):
    j=0
    while(i+j<len(s)):
        if DNAcodon(s[i+j:i+j+3])=="M":
            k=j+3
            prot="M"
            while DNAcodon(s[i+k:i+k+3])!="_" and i+k<len(s):
                prot=prot+DNAcodon(s[i+k:i+k+3])
                k=k+3
            if DNAcodon(s[i + k:i + k + 3]) == "_":
                orf.append(prot)
        j=j+3
orfout=[]
for i in orf:
    if i not in orfout:
        print(i)
        orfout.append(i)

