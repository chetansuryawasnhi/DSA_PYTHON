m=4
arr=[[1],[1,1]]
for i in range(m):
            ar=[]
            ar.append(1)
            for j in range(1,len(arr[-1])):
                ar.append(arr[j-1]+arr[j])
            ar.append(1)
            arr.append(ar)
print(arr)