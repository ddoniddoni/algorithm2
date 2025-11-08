import sys
input = sys.stdin.readline
from collections import deque

direction = [(1,0), (-1, 0), (0, 1), (0, -1)]

def bfs(n, m):
    dq = deque()
    dq.append((n, m))
    visited[n][m] = True
    temp[n][m] = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    temp[nx][ny] = temp[x][y] + 1
                    dq.append((nx, ny))
                    

N, M = map(int, input().split())
maps = []
visited = [[False] * M for _ in range(N)]
temp = [[0] * M for _ in range(N)]

for _ in range(N):
    maps.append(list(map(int, input().strip())))

bfs(0,0)
print(temp[N-1][M-1])