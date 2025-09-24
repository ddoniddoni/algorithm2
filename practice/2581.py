import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
ret = []

def is_prime(n):
    if n >= 2:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True


for num in range(M, N+1):
    if is_prime(num):
        ret.append(num)

if len(ret) == 0:
    print(-1)
else:
    print(sum(ret))
    print(ret[0])



# for n in range(M, N+1):
#     if n < 2:
#         continue
#     else:
#         is_prime = True
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             ret.append(n)

# if len(ret) == 0:
#     print(-1)
# else:
#     print(sum(ret))
#     print(ret[0])