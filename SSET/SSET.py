with open(r'C:\Users\kvend\Downloads\rosalind_sset (1).txt') as f:
    lines = f.readlines()
s=lines[0][:-1]
print(2**int(s)%1000000)