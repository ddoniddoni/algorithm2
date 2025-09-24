import sys
input = sys.stdin.readline

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N+1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

dp = [0] * (N + 2)

for i in range(1, N+1):
    dp[i+1] = max(dp[i+1], dp[i])

    if i + T[i] <= N + 1:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])
print(max(dp))