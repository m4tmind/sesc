k=[]
n=[]
a=int(input())
while a!=0:
    a=int(input())
    if a>0 and a%2==0:
        k.append(a)
for i in k:
    n.append(min(k))
    n.append(max(k))
    break
print(*n)