v=4
g=[[0,2,1],[1,0,2],[1,3,7],[3,2,10],[3,1,3]]
mat=[[float("inf")]*v for i in range(v)]
print(mat)
for s,e,d in g:
    mat[s][e]=min(mat[s][e],d)
for k in range(v):
    for i in range(v):
        for j in range(v):
            if i==j:
                mat[i][j]=0
            else:
                mat[i][j]=min(mat[i][j],mat[i][k]+mat[k][j])
for i in mat:
    print(i)