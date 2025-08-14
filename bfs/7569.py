import sys
from collections import deque
input = sys.stdin.readline

# 익은건 1, 익지 않은 토마토 0, 토마토가 들어있지 않은 칸 -1

m, n, h = map(int, input().split())

boxes = []
for _ in range(h):
    floor = [list(map(int, input().split())) for _ in range(n)]
    boxes.append(floor)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if boxes[z][x][y] == 1:
                q.append((z, x, y))

while q :
    z, x, y = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if boxes[nz][nx][ny] == 0:
                boxes[nz][nx][ny] = boxes[z][x][y] + 1
                q.append((nz,nx,ny))

answer = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if boxes[z][x][y] == 0:
                print(-1)
                sys.exit(0)
            answer = max(answer, boxes[z][x][y])
print(answer - 1)


