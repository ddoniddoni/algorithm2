import sys
input = sys.stdin.readline

n = int(input())
max_n = 40

zero = [0] * (max_n + 1)
one = [0] * (max_n + 1)

zero[0], one[0] = 1,0
zero[1], one[1] = 0,1

for i in range(2, max_n + 1):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

for _ in range(n):
    n = int(input())
    print(zero[n], one[n])



