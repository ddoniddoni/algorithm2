import sys
input = sys.stdin.readline

count = int(input())
nums = list(map(int, input().split()))

sorted_unique = sorted(set(nums))

index_dict = {num: idx for idx, num in enumerate(sorted_unique)}


print(' '.join(str(index_dict[num]) for num in nums))