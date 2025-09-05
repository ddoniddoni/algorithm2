import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
# visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

visited = [False] * (n+1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    count = 0
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1
    return count

print(bfs(1))