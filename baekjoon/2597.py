arr=[]
cnt=0
for _ in range(5):
    arr.append(int(input()))
arr.sort()
for i in arr:
    cnt=cnt+i
print(int(cnt/5))
print(arr[2])