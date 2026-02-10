def f(n):
    i=2
    while i*i<=n:
        if n%i==0:
            print('composite')
            break
        i+=1
    else:
        print('prime')
n=int(input())
f(n)