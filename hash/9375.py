import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cnt = int(input())
    clothes = {}
    for _ in range(cnt):
        name, kind = input().split()
        if kind not in clothes:
            clothes[kind] = 1
        else:
            clothes[kind] += 1
    answer = 1
    for kind in clothes:
        answer *= (clothes[kind] + 1)
    answer -= 1

    print(answer)
    