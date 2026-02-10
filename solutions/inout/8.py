a=int(input())
c=a//1000
d=a%10
n=(c-d)//10
m=(a-c*1000-n*10-d)
if c==d and n==m:
    print(1)
else:
    print(0)