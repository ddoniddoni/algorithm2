import sys
input = sys.stdin.readline

n = int(input())

answer = n
for _ in range(n):
    seen = set()
    s = input().strip()
    prev = ''

    for ch in s:
        if ch != prev:
            if ch in seen:
                answer -= 1
                break
            seen.add(ch)
        prev = ch
print(answer)