def fun(ind,arr,arr2,re):
    if ind>=len(arr):
            # print(arr2)
            re.append(arr2.copy())
            # print(re)
            return True
    arr2.append(arr[ind])
    l=fun(ind+1,arr,arr2,re)
    if not l:
        arr2.remove(arr[ind])
        fun(ind+1,arr,arr2,re)
    return re
print(fun(0,[1,2,1],[],[]))