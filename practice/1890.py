import sys
input = sys.stdin.readline

N = int(input())
wall = []
for _ in range(N):
    wall.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j] != 0 and not (i == N-1 and j == N-1):
            jump = wall[i][j]
            if i + jump < N:
                dp[i + jump][j] += dp[i][j]
            if j + jump < N:
                dp[i][j + jump] += dp[i][j]

print(dp[N-1][N-1])
print(dp)
