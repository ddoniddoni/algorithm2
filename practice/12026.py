import sys
input = sys.stdin.readline

N = int(input())
street = input().strip()

INF = float("inf")
dp = [INF] * N
dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if street[j] == 'B' and street[i] == 'O':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        elif street[j] == 'O' and street[i] == 'J':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        elif street[j] == 'J' and street[i] == 'B':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)


print(dp[-1] if dp[-1] != INF else -1)