import sys
input = sys.stdin.readline

n = int(input())

worker = set()

for _ in range(n):
    user, action = input().split()
    if action == 'leave':
        worker.remove(user)
    else:
        worker.add(user)

for name in sorted(worker, reverse=True):
    print(name)