import sys
input = sys.stdin.readline


def dfs(start):
    if len(answer) == 6:
        print(*answer)
        return
    
    for i in range(start, k):
        answer.append(nums[i])
        dfs(i + 1)
        answer.pop()

while True:
    line = input().split()
    if line[0] == '0':
        break

    k = int(line[0])
    answer = []
    nums = list(map(int, line[1:]))
    dfs(0)
    print()
