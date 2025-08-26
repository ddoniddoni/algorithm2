import sys
input = sys.stdin.readline

num = int(input())
t = [list(map(int, input().split())) for _ in range(num)]

dp = [[0] * num for _ in range(num)]
dp[0][0] = t[0][0]

for i in range(1, num):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + t[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + t[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + t[i][j]

print(max(dp[num-1]))