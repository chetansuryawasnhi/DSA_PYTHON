from typing import List
import heapq
import math
def dijkstra(V: int, adj: List[List[int]], S: int) -> List[int]:
        dis=[math.inf]*V
        print(dis)
        dis[S]=0
        min_heap=[(0,S)]
        while min_heap:
            dist,node=heapq.heappop(min_heap)
            # if d>dis[n]:
            #     continue
            for adjnode,edwei in adj[node]:
                if dist+edwei<dis[adjnode]:
                    dis[adjnode]=dist+edwei
                    heapq.heappush(min_heap, (dis[adjnode], adjnode))
            return dis
k=dijkstra(4,[[[1,9],[2,1],[3,1]],[[3,3]],[[3,2]]],0)
print(k)