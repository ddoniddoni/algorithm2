import sys
input = sys.stdin.readline

n = int(input())
people = sorted(map(int, input().split()))

start, mid, end = 0, n // 2, n-1
answer = 0

for i in range(n-2):
    left, right = i+1, n-1
    while left < right:
        s = people[i] + people[left] + people[right]
        if s == 0:
            if people[left] == people[right]:
                cnt = right - left + 1
                answer += cnt * (cnt - 1) // 2
                break
            else:
                l_cnt, r_cnt = 1, 1
                while left + 1 < right and people[left] == people[left + 1]:
                    l_cnt += 1
                    left += 1
                while right - 1 > left and people[right] == people[right - 1]:
                    r_cnt += 1
                    right -= 1
                
                answer += l_cnt * r_cnt
                left += 1
                right -= 1

        elif s < 0:
            left += 1
        else:
            right -= 1
    
print(answer)