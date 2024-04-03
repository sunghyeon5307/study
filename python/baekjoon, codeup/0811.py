# 1
count = 0
N = 120
i = 1
while i <= N:
    if N%i==0:
        print(i)
        count += 1 
    i += 1
print(f"{N}의 약수는 총{count}개입니다.")

# 2
i = 1
a = 0
b = 1
while i < 51:
    print(b)
    result = a 
    a = b 
    b += result
    i += 1
  
# 3
i = 1
while i < 10:
    j = 1
    while j < 10:
        print("{} * {} = {}".format(i, j, i*j))
        j += 1
    i += 1
