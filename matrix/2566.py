import sys
input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(9)]

row = 0
col = 0
max_value = -1

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            row = i
            col = j

print(max_value)
print(row + 1, col + 1)