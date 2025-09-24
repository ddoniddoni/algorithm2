from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def bfs(a,b):
    q = deque([(a, 1)])
    while q:
        val, cnt = q.popleft()
        if val == b:
            return cnt
        if val * 2 <= b:
            q.append((val * 2, cnt + 1))
        if val * 10 + 1 <= b:
            q.append((val * 10 + 1, cnt + 1))
    return -1

print(bfs(N,M))
