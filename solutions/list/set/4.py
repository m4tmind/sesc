a=input().split()
k=0
c=sorted(set(a))
for i in a:
    if i in a:
        k+=1
    if k>0:
        print('YES')
    else:
        print('NO')
