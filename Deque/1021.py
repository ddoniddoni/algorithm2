import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
target_numbers = list(map(int, input().split()))
answer = 0

dqe = deque(range(1, n+1))

for target in target_numbers:
    idx = dqe.index(target)
    
    if idx <= len(dqe) // 2:
        dqe.rotate(-idx)
        answer += idx
    else:
        dqe.rotate(len(dqe) - idx)
        answer += len(dqe) - idx
    dqe.popleft()

print(answer)