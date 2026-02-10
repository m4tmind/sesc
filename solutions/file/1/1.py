k=[]
n=[]
c=0
f=open('input.txt','r')
for i in f:
    if i>0 and i%2==0:
        k.append(i)
        for i in k:
            n.append(min(i))
            n.append(max(i))
            c+=1
f.close()
of=open('output.txt','w')
if c!=0:
    of.write(*n)
else:
    of.write('0')
of.close