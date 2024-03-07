a = []
n = input()

for i in range(19):
    a.append([])
    for j in range(19):
        a[i].append(0)

for i in range(n):
    x, y = input().split()
    a = [x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(a[i][j], end=' ')
    print()