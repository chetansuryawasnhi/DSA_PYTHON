from collections import deque
g=[[1,2],[1,3],[1,4],[3,4],[4,5]]
v=5
sta=1
dis=5
st=[[] for i in range(v+1)]
re=[]
dist = [0]*(v+1)
q=deque()
par=[-1]*(v+1)
par2=[-1]*(v+1)
for i ,j in g:
    st[i].append(j)
    st[j].append(i)
print(st)
q.append(sta)
while q:
    curr=q.popleft()
    re.append(curr)
    for i in st[curr]:
        if dist[i]==0:
            par[i]=curr
            q.append(i)
            dist[i]=(dist[curr]+1)

print(re,dist,par)
path = []
path2=[]
current_node = dis
path.append(dis)
while par[current_node] != -1:
        path.append(par[current_node])
        current_node = par[current_node]

    # Printing path from source to destination
for i in range(len(path) - 1, -1, -1):
        print(path[i], end=" ")