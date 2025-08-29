import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
n_array = sorted(map(int, input().split()))

m = int(input())
m_array = list(map(int, input().split()))

for ma in m_array:
    idx = bisect_left(n_array, ma)
    if idx < len(n_array) and n_array[idx] == ma:
        print(1, end=' ')
    else:
        print(0, end=' ')