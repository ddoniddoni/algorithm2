import sys
input = sys.stdin.readline

n,m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = []
numbers.sort()
visited = [False] * n

def dfs():
    if len(answer) == m:
        print(*answer)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(numbers[i])
            dfs()
            answer.pop()
            visited[i] = False

dfs()
    