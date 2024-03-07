# 6094
n = int(input())
a = input().split()
for i in range(n):
  a[i] = int(a[i])
min = a[0]
for i in range(0, n):
  if a[i]<min:
    min = a[i]
print(min)

# 6095
d=[]                    
for i in range(20) :
  d.append([])       
  for j in range(20) : 
    d[i].append(0) 

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1 

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')
  print()               

# 6069
# 딕셔너리 2줄로 풀기
a = {'A':"best!!!", 'B':"good!!", 'C':"run!", 'D':"slowly~"}
print(a.get(input(), "what?"))

# 6070
num = int(input())
if num in [12,1,2]:
  print("winter")
elif num in [3,4,5]:
  print("spring")
elif num in [6,7,8]:
  print("summer")
elif num in [9,10,11]:
  print("fall")