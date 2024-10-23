arr=[4,5,8,1,1,2,4,6]
seg=[0]*(5001)
def build(ind,low,high):
    # print(ind,low,high)
    if (low==high):
        seg[ind]=arr[low]
        return
    mid=(low+high)//2
    build(2*ind+1,low,mid)
    build(2*ind+2,mid+1,high)
    seg[ind]=max(seg[2*ind+1],seg[2*ind+1])

def query(ind,low,high,l,r):
    if low>=l and high<=r:
        return seg[ind]
    if high<l or low>r:
        return float("-inf")
    mid=(low+high)//2
    left=query(2*ind+1,low,mid,l,r)
    right=query(2*ind+2,mid+1,high,l,r)
    return max(left,right)
    
build(0,0,len(arr)-1)
print(query(0,0,len(arr)-1,3,6))