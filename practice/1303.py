import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
people = [list(input().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(a, b, color):
    q = deque([(a, b)])
    visited[a][b] = True
    count = 1

    while q:
        x, y = q.popleft()
        for dx, dy in dt:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and people[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

my = 0
enemy = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            color = people[i][j]
            size = bfs(i, j, color)
            if color == 'W':
                my += size ** 2
            else:
                enemy += size ** 2

print(my, enemy)


            