import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
wall = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dist = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0

for _ in range(K):
    x, y = map(int, input().split())
    wall[x-1][y-1] = '#'

def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = True
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dist:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and wall[nx][ny] == '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

for i in range(N):
    for j in range(M):
        if not visited[i][j] and wall[i][j]:
            answer = max(bfs(i, j), answer)

print(answer)
