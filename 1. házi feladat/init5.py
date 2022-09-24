with open(r'C:\Users\kvend\Downloads\rosalind_ini5.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    if i%2==1:
        print(str(lines[i][0:-1]))