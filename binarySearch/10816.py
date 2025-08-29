import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n = int(input())
n_array = sorted(map(int, input().split()))

m = int(input())
m_array = list(map(int, input().split()))

# count_dict = {}
# for num in n_array:
#     if num in count_dict:
#         count_dict[num] += 1
#     else:
#         count_dict[num] = 1

# print(count_dict)

# answer = [str(count_dict.get(num, 0)) for num in m_array]
# print(' '.join(answer))


for num in m_array:
    left = bisect_left(n_array, num)
    right = bisect_right(n_array, num)
    print(right - left, end=' ')