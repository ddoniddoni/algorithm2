import sys
input = sys.stdin.readline

num = input()
arr = list(map(int, input().split()))

print(min(arr), max(arr))