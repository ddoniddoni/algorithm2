import sys
input = sys.stdin.readline

N,M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    answer = []
    for j in range(M):
        answer.append(A[i][j] + B[i][j])
    print(*answer)
