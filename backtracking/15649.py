import sys
input = sys.stdin.readline

n, m = map(int, input().split())
used = [False] * (n + 1)
path = []
answer = []

def dfs(dep):
    if dep == m:
        print(" ".join(map(str,path)))
        return
    for i in range(1, n+1):
        if not used[i]:
            used[i] = True
            path.append(i)
            dfs(dep + 1)
            path.pop()
            used[i] = False

dfs(0)