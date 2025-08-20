import sys
input = sys.stdin.readline

n = int(input())
cols = set()
diag1 = set()
diag2 = set()
ans = 0

def dfs(r):
    global ans
    if r == n:
        ans += 1
        return
    for c in range(n):
        if c in cols or (r+c) in diag1 or (r - c) in diag2:
            continue
        cols.add(c); diag1.add(r + c); diag2.add(r - c)
        dfs(r+1)
        cols.remove(c); diag1.remove(r + c); diag2.remove(r - c)

dfs(0)
print(ans)
