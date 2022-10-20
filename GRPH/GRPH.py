import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import fasta_reader
import networkx as nx
#Beolvasás
szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_grph.txt')
ertek=[]
for i in range(len(szam)):
    ertek.append((szam[i],DNS[i]))
#Gráf, melyben uv él, ha u utolsó 3 karaktere megegyezik v első 3 karakterével.
G=nx.DiGraph()
G.add_nodes_from(ertek)
for u in G.nodes:
    for v in G.nodes:
        if u != v and u[1][len(u[1])-3:len(u[1])]==v[1][:3]:
            G.add_edge(u, v)
# Az élek kiírása
for e in G.edges:
    print(e[0][0][1:],e[1][0][1:])