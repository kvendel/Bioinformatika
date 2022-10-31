import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import fasta_reader

szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_kmp.txt')
s=DNS[0]
n=len(s)
f=[0]
for i in range(1,n):
    if s[i]==s[f[i-1]]:
        f.append(f[i-1]+1)
    else:
        k=0
        for j in range(f[i-1]):
            if s[:j+1]==s[i-j:i+1]:
                k=j+1
        f.append(k)
print(*f)