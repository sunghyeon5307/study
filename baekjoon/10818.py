n=int(input())
num=list(map(int,input().split()))
min=1000000
max=-1000000
for i in range(n):
    if num[i]>max:
        max=num[i]
    if num[i]<min:
        min=num[i]
print(min, max)