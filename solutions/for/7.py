c=0
k=[]
n=int(input())
for i in range(0,n-1):
    if (i+1)%2==0:
        c=2**(i+1)
        k.append(c)
k.sort(reverse=True)
print(*k)