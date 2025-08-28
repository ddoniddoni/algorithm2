import sys
input = sys.stdin.readline

n, price = map(int, input().split())

coins = [int(input()) for _ in range(n)]

count = 0

for coin in reversed(coins):
    if price >= coin:
        count += price // coin
        price %= coin

print(count)


