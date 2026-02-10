
a=int(input())
b=int(input())
c=int(input())
d=int(input())
for i in range(-1,1000):
    x=i+1
    if a*x**3 + b*x**2 + c*x + d==0:
        print(x, end=" ")
