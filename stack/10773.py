import sys
input = sys.stdin.readline

k = int(input())

answer = []

for _ in range(k):
    num = int(input())
    if num == 0:
        answer.pop()
    else:
        answer.append(num)

if not answer:
    print(0)
else:
    print(sum(answer))