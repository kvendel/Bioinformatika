import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import mass_table

f = open(r'C:\Users\kvend\Downloads\rosalind_prtm.txt')
s=str(f.read())
out=0
for i in range(len(s)-1):
    out=out+mass_table(s[i])
print(out)