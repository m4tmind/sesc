l=list(map(int,input().split()))
mn=0
for i in l:
    if i%2==1:
        if i<mn or mn%2==0:
            mn=i
print(mn)