a,i=map(int,input().split())
print(a^(1<<i))
'''b=0
c=bin(a)[2:][::-1]
for j in range(len(c)):
    if j==i and c[i]=='1':
        j='0'
    elif j==i and c[i]=='0':
        b=1
print(b)'''