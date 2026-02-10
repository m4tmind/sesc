a=int(input())
b=int(input())
c=0
while a!=b and a>b:
    if a%2==0 and a//2>b:
        a//=2
        c=':2'
        print(c)
    else:
        a-=1
        c='-1'
        print(c)