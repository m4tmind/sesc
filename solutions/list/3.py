l=list(map(int,input().split()))
for i in range(0, len(l)):
    if i>=1:
        if (l[i]>0 and l[i-1]>0) or (l[i]<0 and l[i-1]<0):
            print(l[i-1],l[i])
            break