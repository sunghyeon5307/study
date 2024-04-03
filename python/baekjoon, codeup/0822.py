a = int(input("정수를 입력하세요"))
b = int(input("입력"))
print(a + b)

a, b = input().split()
a = int(a)
b = int(b)
print(a + b)

a = 10
b = 10.5
print(a+b)

str = "hello"
num = 5
result = str*num
print(result)

for i in range(5):
    for j in range(5):
        print(i)

count = 0
while count !=3:
    count += 1
    print("ㅎ")

a = True
if a == True:
    print("O")

num = input()
if num == "A":
    print("best!!!")
elif num == "B":
    print("good!!")
elif num == "C":
    print("run!")
elif num == "D":
    print("slowly~")
else:
    print("what?")

m = int(input())
if m//3==1:
    print("spring")
elif m//3==2:
    print("summer")
elif m//3==3:
    print("fall")
else:
    print("winter")

n = int(input())
for i in range(n):
    result = n
    n -= 1
    print(n)

n = int(input())
for i in range(0, n+1):
    print(i)
    i += 1

n = int(input())
result = 0
for i in range(1, n+1):
    if i % 2 == 0:
        result += i
print(result)

n = int(input())
result = 0
for i in range(1, n):
    result += i
    if result >= n:
        break
print(i)

a, b = input().split()
a = int(a)
b = int(b)
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, j)

a, b, c = input().split()
count = 0
a = int(a)
b = int(b)
c = int(c)
for i in range(0, a):
    for j in range(0,b):
        for k in range(0, c):
            print(i, j, k)
            count += 1
print(count)

a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)
result = 1
for i in range(n + 1):
    result += d
print(result)
