import sys
input = sys.stdin.readline

N = int(input())
answer = 0
for i in range(1, N):
    temp = i + sum(map(int, str(i)))
    if temp == N:
        answer = i
        break

print(answer)