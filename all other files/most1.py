nums =[1,1,1,0,0,0,1,1,1,1,0]
k =2
max1=0
for i in range(len(nums)):
                    c=0
                    for j in range(i,len(nums)):
                        if nums[j]==0:
                            c+=1
                        if c<=k:
                            max1=max(max1,(j-i+1))
                        else:
                            break
print(max1)