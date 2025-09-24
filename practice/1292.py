import sys
input = sys.stdin.readline

A, B = map(int, input().split())
count, total = 0, 0

for num in range(1, B+1):
    for _ in range(num):
        count += 1
        if A <= count <= B:
            total += num

print(total)