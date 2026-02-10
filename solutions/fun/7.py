a=int(input())
b=int(input())
def f(a,b):
    while a!=0 and b!=0:
        (a, b) = (b, a%b)
    return a
print(a//(f(a,b)), b//(f(a,b)))