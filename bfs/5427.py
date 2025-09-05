import sys
from collections import deque
input = sys.stdin.readline

case = int(input().strip())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(case):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]
    
    fire_q = deque()
    sg_q = deque()

    fire_dist = [[-1] * w for _ in range(h)]
    sg_dist = [[-1] * w for _ in range(h)]

    for y in range(h):
        for x in range(w):
            if building[y][x] == '*':
                fire_q.append((y, x))
                fire_dist[y][x] = 0
            if building[y][x] == '@':
                sg_q.append((y, x))
                sg_dist[y][x] = 0

    while fire_q:
        y, x = fire_q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if building[ny][nx] != '#' and fire_dist[ny][nx] == -1:
                    fire_dist[ny][nx] = fire_dist[y][x] + 1
                    fire_q.append((ny, nx))
    
    escaped = False
    while sg_q:
        y, x = sg_q.popleft()

        if y == 0 or y == h-1 or x == 0 or x == w - 1:
            print(sg_dist[y][x]+1)
            escaped = True
            break
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if building[ny][nx] != '#' and sg_dist[ny][nx] == -1:
                    if fire_dist[ny][nx] == -1 or sg_dist[y][x] + 1 < fire_dist[ny][nx]:
                        sg_dist[ny][nx] = sg_dist[y][x] + 1
                        sg_q.append((ny, nx))
        
    if not escaped:
        print("IMPOSSIBLE")



              
   




    