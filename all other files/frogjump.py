
height=[10 ,20, 30, 10]
n=4
dp=[-1]*4
dp[0]=0
for i in range(1,n):
    right=float("inf")
    left=dp[i-1]+abs(height[i]-height[i-1])
    if i>1:
        right=dp[i-2]+abs(height[i]-height[i-2])
    
    dp[i]=min(left,right)
print(dp)
print(dp[-1])