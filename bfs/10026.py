import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

board = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, color, board, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for dx, dy in move:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

not_green = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j], board, visited)
            not_green += 1


for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
green = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j], board, visited)
            green += 1

print(not_green, green)