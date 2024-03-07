# 1901
n = int(input())
def f(n):
    if(n!=0):
        f(n-1)
        print(n)        
f(n)

# 1902
n = int(input())
def f(n):
    if(n!=0):
        print(n)
        f(n-1)
f(n)

# 1904
a,b = map(int, input().split())
def f(a, b):
    if(a>b):
        return
    if(a%2==1):
        print(a)
    f(a+1,b)
f(a,b)

# 1912
n = int(input())
def f(n):
    if(n==0):
        return 1
    return n*f(n-1)
print(f(n))

# 1920
n = int(input())
def f(n):
    if(n==0):
        return
    f(n/2)
    if(n%2==0):
        print("0")
    elif(n%2==1):
        print("1")
f(n)
