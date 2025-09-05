import sys
input = sys.stdin.readline

n,m = map(int, input().split())

sites = {}

for i in range(n):
    site, password = input().split()
    sites[site] = password

for _ in range(m):
    site = input().strip()
    print(sites[site])
