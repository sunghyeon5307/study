# 1413
# s = input()
# for i in range(len(s)-1, -1, -1):
#     print(s[i], end='')

# 1617
a = input()
a = int(a)
if a<10:
    b = a
else:
    for i in range(len(a)-1, -1, -1):
        b = a[i]
num = a+b
if num[0]==num[-1]:
    print('YES')
else:
    print('NO')
# 1618



