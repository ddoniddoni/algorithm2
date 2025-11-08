import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
find_nums = list(map(int, input().split()))

for f_num in find_nums:
    left = bisect_left(nums, f_num)
    right = bisect_right(nums, f_num)
    if right - left > 0:
        print(1)
    else:
        print(0)