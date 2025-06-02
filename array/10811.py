import sys
input = sys.stdin.readline

n,m = map(int, input().split())

baskets = list(range(1, n+1))

for _ in range(m):
    i,j = map(int, input().split())
    temp = baskets[i-1:j]
    temp.reverse()
    baskets[i-1:j] = temp
print(*baskets)