num=int(input())
s=[int(input()) for _ in range(num)]
dp=[0]*(num)
if len(s)<=2:
    print(sum(s))
else: 
    dp[0]=s[0]
    dp[1]=s[0]+s[1]
for i in range(2,num):
    dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
print(dp[-1])