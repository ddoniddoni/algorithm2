import sys
input = sys.stdin.readline

m,n = map(int, input().split())
snacks = list(map(int, input().split()))

left, right = 1, max(snacks)
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = 0
    for s in snacks:
        count += s // mid

    if count >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)