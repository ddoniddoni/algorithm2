import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

start, end = 0, n - 1
best_sum = abs(nums[start] + nums[end])
answer = (nums[start], nums[end])

while start < end:
    s = nums[start] + nums[end]

    if abs(s) < best_sum:
        best_sum = abs(s)
        answer = (nums[start], nums[end])

    if s > 0:
        end -= 1
    elif s < 0:
        start += 1
    else:
        break

print(answer[0], answer[1])



                
            