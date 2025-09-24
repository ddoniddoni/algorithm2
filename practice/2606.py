import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited[start] = True
    answer = 0
    while q:
        temp = q.popleft()
        for g in graph[temp]:
            if not visited[g]:
                visited[g] = True
                answer += 1
                q.append(g)
    return answer

print(bfs(1))

