import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    dfs_answer.append(v)
    for g in sorted(graph[v]):
        if not visited[g]:
            dfs(g)

def bfs(v):
    visited_bfs = [False] * (N + 1)
    q = deque([v])
    visited_bfs[v] = True
    bfs_answer = []
    
    while q:
        temp = q.popleft()
        bfs_answer.append(temp)
        for g in sorted(graph[temp]):
            if not visited_bfs[g]:
                visited_bfs[g] = True
                q.append(g)
    return bfs_answer



N,M,V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_answer = []
dfs(V)




print(dfs_answer)
print(bfs(V))