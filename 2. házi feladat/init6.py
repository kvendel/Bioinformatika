with open('rosalind_ini5 (2).txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    if i%2==1:
        print(str(lines[i][0:-1]))