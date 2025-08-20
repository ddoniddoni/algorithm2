import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
answer = []
#for comb in combinations(range(1, n+1), m):
#    print(*comb)

def dfs(start):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(start, n+1):
        answer.append(i)
        dfs(i + 1)
        answer.pop()

dfs(1)



