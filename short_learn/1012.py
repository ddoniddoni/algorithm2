import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
direction = [(1,0), (-1, 0), (0, 1), (0, -1)]

def bfs(n, m):
    dq = deque()
    dq.append((n, m))
    visited[n][m] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
    return 1


for _ in range(T):
    M, N, K = map(int, input().split())
    maps = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    baechu = []
    for _ in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1 and not visited[i][j]:
                answer += bfs(i, j)

    print(answer)