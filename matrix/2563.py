import sys
input = sys.stdin.readline

count = int(input())
square = [[0] * 100 for _ in range(100)]

for _ in range(count):
    s, e = map(int, input().split())

    for i in range(s, s+10):
        for j in range(e, e + 10):
            square[i][j] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if square[i][j] == 1:
            answer += 1
print(answer)