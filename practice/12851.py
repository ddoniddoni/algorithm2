import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100001
dist = [-1] * MAX
ways = [0] * MAX

q = deque([N])
dist[N] = 0
ways[N] = 1

while q:
    x = q.popleft()
    for nx in (x-1, x+1, x*2):
        print(nx)
        if 0 <= nx < MAX:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                ways[nx] = ways[x]
                q.append(nx)
            elif dist[nx] == dist[x] + 1:
                ways[nx] += ways[x]

print(dist[K])
print(ways[K])