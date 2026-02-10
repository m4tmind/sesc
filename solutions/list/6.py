l=list(map(int,input().split()))
k=[]
if len(l)%2==0:
    for i in range(0,(len(l)//2)):
        if i>=1:
            l[i-1]=l[i]
            k.append(l[i])
elif len(l)%2==1:
    for i in range(0, (len(l)-1)):
        if i>=1:
            l[i-1]=l[i]
        k.append(l[i])
print(*k)