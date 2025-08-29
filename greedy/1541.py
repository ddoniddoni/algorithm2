import sys
input = sys.stdin.readline

cal = input().strip().split('-')

answer = sum(map(int, cal[0].split('+')))

for c in cal[1:]:
    answer -= sum(map(int, c.split('+')))

print(answer)