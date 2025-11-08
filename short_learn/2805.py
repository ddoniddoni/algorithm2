import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total >= M:
        result = mid
        low = mid + 1
    else:
        high = mid - 1
print(result)