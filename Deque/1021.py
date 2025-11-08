import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
nums = list(map(int, input().split()))

dq = deque(range(1, N+1))
answer = 0

for n in nums:
    idx = dq.index(n)

    if idx <= len(dq) // 2:
        answer += idx
        dq.rotate(-idx)
    else:
        answer += len(dq) - idx
        dq.rotate(len(dq)-idx)
    
    dq.popleft()

print(answer)