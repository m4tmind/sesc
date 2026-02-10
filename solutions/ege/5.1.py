n=int(input())
m=n
t=0
s=''
k=''
y=1
while n>0:
    s+=str(n%3)
    n//=3
s=s[::-1]
if m%3==0:
    s=s+s[-2::]
    print(int(s,3))
else:
    for i in s:
        t+=int(i)
    y=t*3
    while y>0:
        k+=str(y%3)
        y//=3
    k=k[::-1]
    t=s+k
    print(int(t,3))