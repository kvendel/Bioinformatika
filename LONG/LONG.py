import  sys, os
DN=os.path.dirname(__file__)
PDN=os.path.join(DN,"..")
sys.path.append(PDN)
from utils import fasta_reader
import networkx as nx
szam,DNS=fasta_reader(r'C:\Users\kvend\Downloads\rosalind_long.txt')
ertek=[]
for i in range(len(szam)):
    ertek.append((szam[i],DNS[i]))
G=nx.DiGraph()
G.add_nodes_from(ertek)
d={}
for u in G.nodes:
    for v in G.nodes:
        m=0
        for i in range(max(len(v[1]),len(u[1]))):
            if v[1][0:i+1]==u[1][-2-i:-1] and i>m:
                m=i
        if m>=max(len(v[1]),len(u[1]))/2 and u != v:
            G.add_edge(u, v)
            d[u]=v[1][m+2:]
for u in G.nodes:
    if G.in_degree(u)==0:
        v=u
sorrend=[v]
for i in range(len(G.nodes)-1):
    v=list(G.out_edges(v))[0][1]
    sorrend.append(v)
out=sorrend[0][1]
for i in range(len(sorrend)-1):
    out=out+d[sorrend[i]]
print(out)