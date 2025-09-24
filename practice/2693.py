import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    array = list(map(int, input().split()))
    array.sort(reverse=True)
    print(array[2])