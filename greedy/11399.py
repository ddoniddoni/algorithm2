import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()
answer = 0
temp = 0
for time in times:
    temp += time
    answer += temp
print(answer)