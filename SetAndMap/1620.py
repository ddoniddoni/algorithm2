import sys
input = sys.stdin.readline

n,m = map(int, input().split())

name_num = dict()
num_name = dict()

for i in range(1, n+1):
    name = input().strip()
    name_num[name] = i
    num_name[i] = name

for _ in range(m):
    query = input().strip()
    if query.isdigit():
        print(num_name[int(query)])
    else:
        print(name_num[query])