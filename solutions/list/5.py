l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    if i>=1:
        if l[i]!=l[i-1]:
            c+=1
print(c+1)