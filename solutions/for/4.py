x=int(input())
c=[]
for i in range(2,x):
    if i<=x and i!=0:
        if x%i==0:
            c.append(i)
print(min(c))