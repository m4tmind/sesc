'''s=input().split()
w=set(s)
print(len(w))'''
lines = []
while True:
    txt=input()
    if txt==" ":
        break
    else:
        lines.append(txt + '\n')
    print(len("".join(lines)))