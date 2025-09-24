import sys
input = sys.stdin.readline

N = int(input())
candy = [list(input().strip()) for _ in range(N)]
result = 0

def check(array):
    max_count = 0

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if array[i][j] == array[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_count = max(max_count, cnt)
        
        cnt = 1
        for j in range(1, N):
            if array[j][i] == array[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_count = max(max_count, cnt)
    return max_count


for i in range(N):
    for j in range(N):
        if j + 1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            print(result, check(candy))
            result = max(result, check(candy))
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if i + 1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            print(result, check(candy))
            result = max(result, check(candy))
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(result)
