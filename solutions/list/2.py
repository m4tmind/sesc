k=[]
c=0
l=(list(map(int, input().split())))
for i in range(0,len(l)):
    if l[i]>0:
        c+=1
print(c)