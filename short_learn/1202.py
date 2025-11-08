import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jew = []
bags = []
for _ in range(N):
    weight, price = map(int, input().split())
    jew.append((weight, price))
for _ in range(K):
    bags.append(int(input()))

jew.sort()
bags.sort()

answer = 0
heap = []
idx = 0

for bag in bags:
    while idx < N and jew[idx][0] <= bag:
        heapq.heappush(heap, -jew[idx][1])
        idx += 1
    
    if heap:
        answer += -heapq.heappop(heap)

print(answer)