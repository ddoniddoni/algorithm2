import sys
input = sys.stdin.readline

n = input()
print(''.join(sorted(n, reverse=True)))