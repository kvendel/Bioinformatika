f = open(r'C:\Users\kvend\Downloads\rosalind_iprb.txt')
s=str(f.read()).split()
k=int(s[0])
m=int(s[1])
n=int(s[2])
out=1-(m*(m-1)/2/4+n*m/2+n*(n-1)/2)/((k+m+n)*(k+m+n-1)/2)
print(out)