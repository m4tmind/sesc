k=int(input())
if ((k%3==0 or k%5==0) or (k-(k//3))%5==0 or (k-(k//5))%3==0) and (k>=5 or k>=3):
    print('YES')
else:
    print('NO')