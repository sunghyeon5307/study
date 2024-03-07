# 1008
A,B = map(int,input().split())
result = A/B
print(result)
1 3
0.3333333333333333

# 10430
A,B,C = map(int,input().split())
a = (A+B)%C
b = ((A%C) + (B%C))%C
c = (A*B)%C
d = ((A%C) * (B%C))%C
print(a)
print(b)
print(c)
print(d)
5 8 4
1
1
0
0

# 2588
a = int(input())
b = int(input())
print(a*(b%10))
print(a*(b%100//10))
print(a*(b//100))
print(a*b)
472
385
2360
3776
1416
181720

# 11382
a,b,c = map(int,input().split())
print(a+b+c)
77 77 7777
7931

# 10171
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")
\ /\
) ( ')
( / )
(__)|

# 10172
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")
|_/|
|q p| /}
( 0 )"""<br> |"^"` |
||_/=\__|
