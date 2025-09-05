import sys
import heapq
input = sys.stdin.readline


n = int(input())
array = []

for _ in range(n):
    x = (int(input()))
    if x != 0:
        heapq.heappush(array, (abs(x), x))
    else:
        if array:
            print(heapq.heappop(array)[1])
        else:
            print(0)

