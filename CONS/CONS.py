import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import fasta_reader
import numpy as np
szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_cons.txt')
m=len(DNS)
n=len(DNS[0])
profile=np.zeros((4,n))
for i in range(m):
    for j in range(n):
        if DNS[i][j]=="A":
            profile[0,j]=profile[0,j]+1
        if DNS[i][j]=="C":
            profile[1,j]=profile[1,j]+1
        if DNS[i][j]=="G":
            profile[2,j]=profile[2,j]+1
        if DNS[i][j]=="T":
            profile[3,j]=profile[3,j]+1
profile=profile.astype(int)
c=np.argmax(profile,0)
consensus=""
for i in range(n):
    if c[i]==0:
        consensus=consensus+"A"
    if c[i] == 1:
        consensus = consensus + "C"
    if c[i] == 2:
        consensus = consensus + "G"
    if c[i] == 3:
        consensus = consensus + "T"
print(consensus)
print("A:",*profile[0])
print("C:",*profile[1])
print("G:",*profile[2])
print("T:",*profile[3])