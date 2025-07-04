import sys
input = sys.stdin.readline

count = int(input())
nums = list(map(int, input().split()))
answer = 0

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for num in nums:
    if is_prime(num):
        answer += 1

print(answer)