# 반복문
a, b = map(int, input().split())
while(b!=0):
    a, b = b, a%b
print(a)

# 재귀함수
def f(a, b):
    if a%b == 0:
        return b
    return f(b, a%b)

a, b = map(int, input().split())
print(f(a, b))