n = int(input())
I = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
s = 0
for i in I:
    while(n>=i):
        n = n - i 
        s = s + 1
print(s)