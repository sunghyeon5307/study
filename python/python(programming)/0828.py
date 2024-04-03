n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

b = []
for i in range(0, 23):
    b.append(0)
for i in range(0, 23):
    b[a[i]] += 1
for i in range(0, 23):
    print(b[i], end='')

n = int(input())
num = list(map(int, input().split()))
result = list(0 for _ in range(24))

for i in range(n):
    result[num[i]]+=1

for i in range(1, 24):
    print(result[i], end = ' ')

# split 쓰임, 함수 쓰임 공부하기