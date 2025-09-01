import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = map(int, input().split())

start, end = 0, max(trees)
answer = 0

while start <= end:
    mid = (start + end) // 2
    w = 0
    for t in trees:
        if t > mid:
            w += t - mid
    
    if w >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1


print(answer)
    

