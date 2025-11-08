import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

for comb in combinations(cards, 3):
    total = sum(comb)
    if total <= M:
        answer = max(answer, total)


print(answer)