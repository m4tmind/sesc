c=list(input().split())
d={}
'''while True:
    c=list(input().split())
    k=c[0]
    s=c[1]
    d[k]=s
    for k,s in d.items():
        if k==k:
            s+=s
    print(k,d[k])'''
for k in c:
    if k in d.keys():
        d[k]+=1
    else:
        d[k]=1
c.sort()
print(c[0])