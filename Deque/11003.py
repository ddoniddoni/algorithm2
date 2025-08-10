import sys
from collections import deque
input = sys.stdin.readline

n,l = map(int, input().split())
arr = list(map(int, input().split()))

dqe = deque()
answer = []

for i in range(n):
    while dqe and dqe[-1][0] > arr[i]:
        dqe.pop()
    
    dqe.append((arr[i], i))

    if dqe[0][1] <= i - l:
        dqe.popleft()

    answer.append(dqe[0][0])

print(" ".join(map(str, answer)))