import sys
input = sys.stdin.readline

num = int(input())
array = []
for _ in range(num):
    x, y = map(int, input().split())
    array.append((x,y))

array.sort()

for x, y in array:
    print(x, y)