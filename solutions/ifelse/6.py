x,y=map(float, input().split())
a=2
if x<2 and y>0 and x**2>(4-y**2) and x>y:
    print('YES')
else:
    print('NO')
