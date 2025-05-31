import sys
input = sys.stdin.readline

array_length = int(input())
nums = list(map(int, input().split()))
find_num = int(input())

print(nums.count(find_num))