k=[]
n=[]
c=0
f=open('input.txt','r')
a=f.readline()
while a!='':
    for i in f:
        if int(i)>0 and int(i)%2==0:
            k.append(i)
            for i in k:
                n.append(min(k))
                c+=1
                n.append(max(k))
                c+=1
                break
f.close()
of=open('output.txt','w')
if c!=0:
    of.write(*n)
else:
    of.write('0')
of.close