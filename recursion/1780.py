import sys
input = sys.stdin.readline

n = int(input())

counts = {-1 : 0, 0: 0, 1: 0}

papers = [list(map(int, input().split())) for _ in range(n)]


def check(x, y, size):
    start = papers[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if papers[i][j] != start:
                return False
    return True

def confirm(x, y, size):
    if check(x, y, size):
        counts[papers[x][y]] += 1
        return
    new_size = size // 3
    for dx in range(3):
        for dy in range(3):
            confirm(x + dx*new_size, y + dy*new_size, new_size)

confirm(0, 0, n)
print(counts)