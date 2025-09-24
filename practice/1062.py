import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
words = [set(input().strip()) for _ in range(N)]
print(words)
basic = {'a', 'n', 't', 'i', 'c'}

if K < 5:
    print(0)
    exit()

candidates = set()
for word in words:
    candidates |= (word - basic)


if len(candidates) <= K - 5:
    print(N)
    exit()

answer = 0
for comb in combinations(candidates, K - 5):
    teach = set(comb) | basic
    cnt = 0
    for word in words:
        if word <= teach:
            cnt += 1
    answer = max(answer, cnt)

print(answer)