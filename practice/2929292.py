import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
grpah = [[] for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int, input().split())
    grpah[a].append(b)
    grpah[b].append(a)


def dfs(v):
    visited[v] = True
    dfs_answer.append(v)
    for g in sorted(grpah[v]):
        if not visited[g]:
            dfs(g)

def bfs(v):
    visited_bfs = [False] * (N + 1)
    q = deque([v])
    visited_bfs[v] = True
    bfs_answer = []
    while q:
        x = q.popleft()
        bfs_answer.append(x)
        for g in sorted(grpah[x]):
            if not visited_bfs[g]:
                visited_bfs[g] = True
                q.append(g)
    return bfs_answer


visited = [False] * (N+1)
dfs_answer = []

dfs(V)

print(bfs(V))
print(dfs_answer)