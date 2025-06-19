import sys
input = sys.stdin.readline

num = int(input())
array = [int(input()) for _ in range(num)]
array.sort()
for n in array:
    print(n)
