import sys
from collections import deque
input =  sys.stdin.readline

N,M = map(int, input().split())
walls = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dist = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = [[0] * M for _ in range(N)]


def bfs(a,b):
    q = deque([(a, b, 1)])
    visited[a][b] = True
    answer[a][b] = 1
    while q:
        x, y, d = q.popleft()

        for dx, dy in dist:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and walls[nx][ny] == "1":
                    visited[nx][ny] = True
                    answer[nx][ny] = answer[x][y] + 1
                    q.append((nx,ny, d+1))
    print(answer)
    return answer[N-1][M-1]



print(bfs(0, 0))