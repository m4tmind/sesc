n=int(input())
d={}
for i in range(n):
    c=input().split()
    c=list(c)
    for i in c:
        k=c[0]
        s=c[1]
    d[k]=s
w=input()
for k,s in d.items():
    if w==s:
        print(k)
    elif w==k:
        print(d[k])