import sys
input = sys.stdin.readline

s = input().strip()

result = []

for i in range(26):
    alpha = chr(ord('a') + i)
    result.append(s.find(alpha))

print(*result)