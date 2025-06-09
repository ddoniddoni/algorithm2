import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
array = []

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(M, N + 1):
    if is_prime(i):
        array.append(i)

if len(array) == 0:
    print(-1)
else:
    print(sum(array), min(array))



