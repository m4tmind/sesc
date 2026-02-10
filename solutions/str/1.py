s=str(input())
c=0
b=''
for i in s:
    if i=='a':
        b+='b'
        c+=1
    elif i=='A':
        b+='B'
        c+=1
    else:
        b+=i
print(b)
print(c)