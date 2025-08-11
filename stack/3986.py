import sys
input = sys.stdin.readline

n = int(input())
count = 0

for _ in range(n):
    w = input().strip()
    stack = []

    for ch in w:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        count += 1

print(count)
