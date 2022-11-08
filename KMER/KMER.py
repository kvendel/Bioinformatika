import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import fasta_reader

szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_kmer.txt')
DNA=DNS[0]
def printer(n,m,s,t,mer):
    if n==0:
        mer.append(t)
        return
    for i in range(m):
        t=t+s[i]
        printer(n-1,m,s,t,mer)
        t=t[:-1]
mer=[]
printer(4,4,["A","C","G","T"],"",mer)
out=[]
for t in mer:
    x=0
    for i in range(len(DNA) - len(t)+1):
        if DNA[i:i + len(t)] == t:
            x=x+1
    out.append(x)
print(*out)