import sys
input = sys.stdin.readline

result = []

n = int(input())
cards = set(map(int, input().split()))

m = int(input())
findCards = list(map(int, input().split()))

for f in findCards:
    if f in cards:
        result.append("1")
    else:
        result.append("0")

print(' '.join(result))