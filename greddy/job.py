Jobs = [[1,4,20],[2,1,1],[3,1,40],[4,1,30]]
Jobs.sort(key=lambda x:x[2],reverse=True)
n=max(Jobs,key=lambda x:x[1])[1]
proit=0
c=0
arr=[-1]*(n+1)
for i in Jobs:
    slo=i[1]
    while slo>0:
            if arr[slo]==-1:
                arr[slo]=1
                proit+=i[2]
                c+=1
                break
            slo-=1
print(c,proit,arr)
            
            
        
        