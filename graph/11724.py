import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ad = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    ad[u].append(v)
    ad[v].append(u)

def dfs(x):
    visited[x] = True
    for a in ad[x]:
        if not visited[a]:
            dfs(a)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)