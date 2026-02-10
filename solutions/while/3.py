a=int(input())
s=0
while a!=0:
    c=a%10
    s+=c
    a=(a-c)//10
print(s)
