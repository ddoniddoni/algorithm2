import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input().strip())

for _ in range(n):
    action = input().split()
    command = action[0]
    if command == "push_front":
        q.appendleft(int(action[1]))
    elif command == "push_back":
        q.append(int(action[1]))
    elif command == "pop_front":
        print(q.popleft() if q else -1)
    elif command == "pop_back":
        print(q.pop() if q else -1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        print(0 if q else 1)
    elif command == "front":
        print(q[0] if q else -1)
    elif command == "back":
        print(q[-1] if q else -1)   


