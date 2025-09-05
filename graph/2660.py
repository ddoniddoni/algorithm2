import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (n+1)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return max(dist[1:])


scores = [0] * (n+1)
min_score = n+1

for i in range(1, n+1):
    scores[i] = bfs(i)
    min_score = min(min_score, scores[i])

votes = [i for i in range(1, n+1) if scores[i] == min_score]

print(min_score, len(votes))
print(*votes)