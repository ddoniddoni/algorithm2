import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
maxN = max(nums)

dp = [[0] * 4 for _ in range(maxN + 1)]
dp[1][1] = 1

if maxN >= 2:
    dp[2][1] = 1
    dp[2][2] = 1

if maxN >= 3:
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1

for i in range(4, maxN + 1):
    dp[i][1] = 1
    dp[i][2] = dp[i-2][1] + dp[i-2][2]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]

for n in nums:
    print(dp[n][1] + dp[n][2] + dp[n][3])