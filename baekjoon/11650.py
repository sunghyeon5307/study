n=int(input())
point=[]
for i in range(n):
    a,b=map(int,input().split())
    point.append((a,b))
point.sort()
for x,y in point:
    print(x,y)