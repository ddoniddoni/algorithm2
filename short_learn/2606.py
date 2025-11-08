import sys
input = sys.stdin.readline
from collections import deque


def bfs(n):
    dq = deque()
    dq.append(n)
    visited[n] = True
    count = 0
    while dq:
        i = dq.popleft()
        for num in graph[i]:
            if not visited[num]:
                visited[num] = True
                count += 1
                dq.append(num)
    return count


N = int(input())
C_N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(C_N):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = bfs(1)
print(answer)
