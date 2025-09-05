import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    dfs_order.append(str(v))
    for nx in graph[v]:
        print(nx)
        if not visited[nx]:
            dfs(nx)

def bfs(start):
    q = deque([start])
    visited_bfs = [False] * (N + 1)
    visited_bfs[start] = True
    order = []
    while q:
        cur = q.popleft()
        order.append(str(cur))
        for nx in graph[cur]:
            if not visited_bfs[nx]:
                visited_bfs[nx] = True
                q.append(nx)
    return order

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for adj in graph:
    adj.sort()

print(graph)
visited = [False] * (N + 1)
dfs_order = []
dfs(V)

bfs_order = bfs(V)

print(" ".join(dfs_order))
print(" ".join(bfs_order))