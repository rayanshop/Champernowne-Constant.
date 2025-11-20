b=[]
n=int(input("enter number"))
for i in range(1,n+1):
    a=str(i)
    for j in range(0,len(a)):
        b.append(int(a[j]))
print(b[0:n])