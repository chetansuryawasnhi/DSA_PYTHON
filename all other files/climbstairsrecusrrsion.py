n=4
dp=[-1]*n
def f(n,dp):
    if n==0 or n==1:
        return 1
    if dp[n-1]!=-1:
        return dp[n]
    return f(n-1,dp)+f(n-2,dp)
print(f(n,dp))
