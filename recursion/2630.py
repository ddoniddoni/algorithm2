import sys
input = sys.stdin.readline

n = int(input())

papers = [list(map(int, input().split())) for _ in range(n)]

counts = {0: 0, 1: 0}

def check(x, y, size):
    start = papers[x][y]
    for i in range(x, size+x):
        for j in range(y, size+y):
            if papers[i][j] != start:
               return False
    return True

def confirm(x, y, size):
    if check(x, y, size):
        counts[papers[x][y]] += 1
        return
    
    new_size = size // 2
    confirm(x, y, new_size)
    confirm(x, y + new_size, new_size)
    confirm(x + new_size, y, new_size)
    confirm(x + new_size, y + new_size, new_size)

confirm(0, 0, n)

print(counts[0])
print(counts[1])
            
