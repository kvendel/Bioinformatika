import networkx as nx
with open(r'C:\Users\kvend\Downloads\rosalind_gasm (4).txt') as f:
    lines = f.readlines()
mers2=[]
for i in range(len(lines)):
    mers2.append(lines[i][:-1])
n=len(mers2[0])
#mers2=["AATCT","TGTAA","GATTA","ACAGA"]
mers=[] # Itt lesznek a k+1 merek és az ő inverz-komplementereik.
for i in range(len(mers2)):
    mers.append(mers2[i])
for m in mers2:
    rm=""
    for i in range(len(m)):
        if m[i]=="A":
            rm=rm+"T"
        if m[i]=="T":
            rm=rm+"A"
        if m[i]=="G":
            rm=rm+"C"
        if m[i]=="C":
            rm=rm+"G"
    rm=rm[::-1]
    mers.append(rm)
#---------------------------------------
for k in range(2,n):
    kmers = [] # Itt vannak a k-merek.
    G = nx.DiGraph()
    for mer in mers:
        for i in range(len(mers[0])-k+1):
            part = mer[i:i+k]
            if part not in kmers:
                kmers.append(part)
                G.add_edge(part[:-1], part[1:]) #A de Bruijn gráf csúcsai a k-1-merek.
    H = G.to_undirected()
    if nx.number_connected_components(H) == 2:
        l=list(list(nx.connected_components(H))[1]) #Nézzük az első komponenst.
        #Innen csak a pcov-ot másoltam ki, amely megoldja a feladatot.
        m = l[0]
        out = ""
        for j in range(len(l)):
            i = 0
            while (m[1:] != l[i][:-1] or m == l[i]):
                i = i + 1
            out = out + m[0]
            m = l[i]
        print(out)
        break

