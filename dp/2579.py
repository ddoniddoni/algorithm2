import sys
input = sys.stdin.readline

n = int(input())
st = [int(input()) for _ in range(n)]

if n == 1:
    print(st[0])
elif n == 2:
    print(st[0] + st[1])
else:
    dp = [0] * n
    dp[0] = st[0]
    dp[1] = st[0] + st[1]
    dp[2] = dp[0] + st[2]

    for i in range(3, n):
        dp[i] = max(dp[i-3] + st[i-1] + st[i], dp[i-2] + st[i])

print(dp)


