import sys
from collections import deque
input = sys.stdin.readline


dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x, y, board, visited, m, n):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))


t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    count = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1 and not visited[y][x]:
                bfs(x, y, board, visited, m, n)
                count += 1
    print(board)
    print(visited)
    print(count)