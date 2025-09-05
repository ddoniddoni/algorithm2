import sys
input = sys.stdin.readline

n = int(input())

datas = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        datas.add(name)
    else:
        datas.remove(name)

for name in sorted(datas, reverse=True):
    print(name)