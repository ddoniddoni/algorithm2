import sys
input = sys.stdin.readline

a, b = map(int, input().split())
array = []
for i in range(1, a+1):
    if a % i == 0:
        array.append(i)

if len(array) < b:
    print(0)
else:
    print(array[b-1])