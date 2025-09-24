import sys
input = sys.stdin.readline

N = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def dfs(num, length):
    if length == N:
        print(num)
        return
    for i in range(1, 10):
        new_num = num * 10 + i
        if is_prime(new_num):
            dfs(new_num, length + 1)

for prime in [2,3,5,7]:
    dfs(prime, 1)