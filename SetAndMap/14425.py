import sys
input = sys.stdin.readline


n,m = map(int, input().split())
includedStr = set()
answer = 0

for _ in range(n):
    includedStr.add(input().strip())

for _ in range(m):
    word = input().strip()
    if word in includedStr:
        answer += 1

print(answer)

