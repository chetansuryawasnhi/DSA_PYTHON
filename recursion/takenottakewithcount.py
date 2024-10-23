def fun(ind,sum,arr,t):
    if sum>t:
        return 0
    if ind==len(arr):
        if sum==t:
            return 1
        return 0
    sum+=arr[ind]
    l=fun(ind+1,sum,arr,t)
    sum-=arr[ind]
    r=fun(ind+1,sum,arr,t)
    return l+r
print(fun(0,0,[1,2,1],4))