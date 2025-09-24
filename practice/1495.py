import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
vol = list(map(int, input().split()))
dp = [[False] * (M + 1) for _ in range(N+1)]
dp[0][S] = True

for i in range(1, N+1):
    change = vol[i-1]
    for v in range(M + 1):
        if dp[i-1][v]:
            if v + change <= M:
                dp[i][v + change] = True
            if v - change >= 0:
                dp[i][v-change] = True
        
answer = -1
for v in range(M, -1, -1):
    if dp[N][v]:
        answer = v
        break
print(answer)
print(dp)
