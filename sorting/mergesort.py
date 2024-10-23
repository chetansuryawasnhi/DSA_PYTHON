arr=[4,6,8,2,3,4,5,4,43,8]

def merge_sort(arr,start,end):
    if start>=end:
        return 
    mid=(start+end)//2
    merge_sort(arr,start,mid)
    merge_sort(arr,mid+1,end)
    return merge(arr,start,end,mid)
def merge(arr,start,end,mid):
    k=[]
    l=start
    r=mid+1
    while l<=mid and r<=end:
        if arr[l]<=arr[r]:
            k.append(arr[l])
            l+=1
        else:
            k.append(arr[r])
            r+=1
    while l<=mid:
        k.append(arr[l])
        l+=1
    while r<=end:
        k.append(arr[r])
        r+=1
    print("b",arr)
    for i in range(start,end+1):
        arr[i]=k[i-start]
    print("a",arr)
    return arr
print(merge_sort(arr,0,len(arr)-1))
    