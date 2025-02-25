n=int(input())
point=[]
for _ in range(n):
    a,b=map(int,input().split())
    point.append((a,b))
point.sort(key=lambda x: (x==0,x))
for x,y in point:
    print(x,y)