from collections import deque
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] 
q=deque()
vis=[-1]*5
q.append(0)
vis[0]=1
while q:
    a=q.popleft()
    for i in adj[a]:
        if vis[i]==-1:
            vis[i]=1
            q.append(i)
            print(i)
    

		