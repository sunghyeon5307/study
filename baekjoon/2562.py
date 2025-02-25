max=0
count=0
num=[]
for i in range(9):
    num.append(int(input()))
    if num[i]>max:
        max=num[i]
        count=i+1
print(max)
print(count)