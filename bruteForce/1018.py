import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]

def c_repaint(x, y, start):
    count = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if board[x + i][y + j] != start:
                    count += 1
            else:
                if board[x+i][y+j] == start:
                    count += 1
    return count

min_repaint = 64

for i in range(N - 7):
    for j in range(M - 7):
        repaint_w = c_repaint(i, j, 'W')
        reapint_b = c_repaint(i, j, 'B')
        min_repaint = min(min_repaint, repaint_w, reapint_b)
print(min_repaint)
