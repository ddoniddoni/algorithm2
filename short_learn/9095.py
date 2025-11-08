import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

max_num = max(nums)
dp = [0] * (max_num + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for num in range(4, max_num + 1):
    dp[num] = dp[num-1] + dp[num-2] + dp[num-3]


for num in nums:
    print(dp[num])