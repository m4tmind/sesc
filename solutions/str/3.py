s=input()
c=0
k=s[::-1]
for i in range(len(s)):
    if k==s:
        c+=1
if c==len(s):
    print('YES')
else:
    print('NO')