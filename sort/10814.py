import sys
input = sys.stdin.readline

count = int(input())
users = []

for _ in range(count):
    age, name = input().split()
    users.append((int(age), name))

users.sort(key=lambda x: x[0])

for age,name in users:
    print(age, name)