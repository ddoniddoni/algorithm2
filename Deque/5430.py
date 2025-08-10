import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

for _ in range(n):
    action = input().strip()
    number = int(input())
    str_arr = input().strip()

    if number == 0:
        arr = deque()
    else:
        arr = deque(str_arr[1:-1].split(","))

    isReversed = False
    isError = False
    for cmd in action:
        if cmd == 'R':
            isReversed = not isReversed
        elif cmd == 'D':
            if not arr:
                isError = True
                break
            if isReversed:
                arr.pop()
            else:
                arr.popleft()

    if isError:
        print("error")
    else:
        if isReversed:
            arr.reverse()
        print("[" + ",".join(arr) + "]")