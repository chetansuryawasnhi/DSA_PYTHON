rr="MADAM"
def fun(i,arr):
    if i>=len(arr)//2:
        return True
    elif arr[i]!=arr[len(arr)-1-i]:
        return False
    return fun(i+1,arr)
print(fun(0,rr))