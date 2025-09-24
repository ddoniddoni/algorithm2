import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

start = 0
end = 0
cur_sum = 0
min_length = float('inf')

while True:
    if cur_sum >= S:
        min_length = min(min_length, end - start)
        cur_sum -= numbers[start]
        start += 1
    elif end == N:
        break
    else:
        cur_sum += numbers[end]
        end += 1

print(min_length if min_length != float("inf") else 0)

    
