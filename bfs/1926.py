import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
prints = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(start_r, start_c):
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True
    area = 0

    while q:
        r, c = q.popleft()
        area += 1
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and prints[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return area

count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if prints[i][j] == 1 and not visited[i][j]:
            count += 1
            a = bfs(i,j)
            if a > max_area:
                max_area = a
print(count)
print(max_area)

