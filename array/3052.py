import sys
input = sys.stdin.readline

nums = []

for _ in range(10):
    nums.append(int(input()))

answer = set()

for num in nums:
    answer.add(num % 42)
print(len(answer))