import sys
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    print(a + b)