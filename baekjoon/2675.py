t=int(input())
for _ in range(t):
    r,s=input().split()
    r=int(r)
    arr=s.split()
    for i in s:
        print(i*r,end="")
    print()