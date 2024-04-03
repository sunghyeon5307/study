# 1330
a,b = map(int, input().split())
if a > b:
  print('>')
if a < b:
  print('<')
if a == b:
  print('==')

# 9498
score = int(input())
if 100 >= score >= 90:
  print('A')
elif 89 >= score >= 80:
  print('B')
elif 79 >= score >= 70:
  print('C')
elif 69 >= score >= 60:
  print('D')
else:
  print('F')

# 2753
year = int(input())
result = "1" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0  else "0"
print(result)

# 14681
x= int(input()) 
y= int(input())
if x<0 and y>0:
  print('2')
elif x>0 and y>0:
  print('1')
elif x<0 and y<0:
  print('3')
else:
  print('4')

# 2884
hour,min = map(int,input().split())
if min >= 45:
  print(hour, min-45)
elif hour>0 and min < 45:
  print(hour-1, min+15)
else:
  print(23, min+15)
