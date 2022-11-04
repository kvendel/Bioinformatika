with open(r'C:\Users\kvend\Downloads\rosalind_tree (2).txt') as f:
    lines = f.readlines()
n=int(lines[0][:-1])
print(n-len(lines))