m=int(input())
n=int(input())
k=int(input())
'''if ((m*n)**(k))%4==0 and k!=(m*n):
    print('YES')
else:
    print('NO')'''
if (m*n)%((1/2)**(k/2))==0:
    print('YES')
else:
    print('NO')