import sys
input = sys.stdin.readline

array = [int(input()) for _ in range(5)]

sum_array = sum(array)

print(sum_array // 5)
array.sort()
print(array[2])