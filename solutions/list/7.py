l=list(map(int,input().split()))
k=int(input())
if k<len(l):
    l.remove(l[k])
    print(*l)
else:
    print(*l)