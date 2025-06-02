import sys
input = sys.stdin.readline

num = int(input())
target = input().strip()
answer = 0
for i in range(len(target)):
    answer += int(target[i])

print(answer)

