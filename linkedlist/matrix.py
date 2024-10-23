mat=[[1,2,3],[4,5,6],[7,8,9]]
row,col=3,3
dir=[[0,1],[1,0],[0,-1],[-1,0]]
r,c=0,0  
d=0
for i in range(row*col):
    print(mat[r][c])
    mat[r][c]=-1
    r+=dir[d][0]
    c+=dir[d][1]
    if r<len(mat[0]) and r>=0 and c<len(mat) and c>=0 and mat[r][c]!=-1:
        pass
    else:
        r-=dir[d][0]
        c-=dir[d][1]
        d=(d+1)%4
        r+=dir[d][0]
        c+=dir[d][1]

        
    

            
        

        




    
            
        
    
