import sys
input = sys.stdin.readline

N, M = map(int, input().split())

balls = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for h in range(i - 1, j):
        balls[h] = k

print(*balls)