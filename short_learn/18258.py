import sys
from collections import deque
input = sys.stdin.readline

q = deque()
answer = []
n = int(input())
for _ in range(n):
    action = input().strip().split()

    if action[0] == 'push':
        q.append(action[1])
    elif action[0] == 'front':
        answer.append(q[0] if q else '-1')
    elif action[0] == 'pop':
        answer.append(q.popleft() if q else '-1')
    elif action[0] == 'size':
        answer.append(str(len(q)))
    elif action[0] == 'empty':
        answer.append('1' if not q else '0')
    elif action[0] == 'back':
        answer.append(q[-1] if q else '-1')

print('\n'.join(answer))