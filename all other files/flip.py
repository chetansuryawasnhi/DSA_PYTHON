grid=[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
for i in range(len(grid)):
    if grid[i][0]==0:
        for j in range(len(grid[i])):
            if grid[i][j]==0:
                        grid[i][j]=1
            else:
                        grid[i][j]=0
for j in range(1,len(grid[0])):
    count=0
    for k in range(len(grid)):
        if grid[k][j]==0:
                        count-=1
        else:
                        count+=1
    if count<0:
                for l in range(len(grid)):
                    if grid[l][j]==0:
                        grid[l][j]=1
                    else:
                        grid[l][j]=0
score=0
print(grid)
for i in range (len(grid)):
          for j in range(1,len(grid[i])+1):
            # print(grid[i+1][-j])
            x=(grid[i+1][-j])*(2**(j-1))
            print(x)
            score+=x
          break
print(score)


