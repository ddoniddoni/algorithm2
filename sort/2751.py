import sys
input = sys.stdin.readline

n = int(input())

num_array = [int(input()) for _ in range(n)]

num_array.sort()

for num in num_array:
    print(num)
