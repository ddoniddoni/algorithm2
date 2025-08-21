import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
answer = []
# for comb in combinations(range(1, n+1), repeat=M):
#    print(*comb)

def dfs():
    if len(answer) == m:
        print(*answer)
        return
    for i in range(1, n+1):
        answer.append(i)
        dfs()
        answer.pop()

dfs()