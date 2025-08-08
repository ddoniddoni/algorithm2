import sys
from collections import deque
input = sys.stdin.readline

q = deque()
number = int(input())

for i in range(number):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])

