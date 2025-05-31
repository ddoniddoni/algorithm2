import sys
input = sys.stdin.readline

N, X = map(int, input().split())
array = list(map(int, input().split()))
answer = []

for i in array:
    if i < X:
        answer.append(i)

print(*answer)
