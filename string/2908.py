import sys
input = sys.stdin.readline

N,M = input().split()

r_N = int(N[::-1])
r_M = int(M[::-1])

if r_N > r_M:
    print(r_N)
else:
    print(r_M)


