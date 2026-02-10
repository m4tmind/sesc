c=0
k=[]
n=int(input())
for i in range(1,n):
    if n%i==0:
        c+=i
        k.append(i)
if c==n:
    print(*k)
else:
    print(0)