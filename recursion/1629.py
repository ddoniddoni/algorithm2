import sys
input = sys.stdin.readline

answer = 0

def multi(num, count, div):

    if count == 0:
        return 1 % c

    if count == 1:
        return num % c
    
    half = multi(num, count // 2, div)
    half_sq = (half * half) % div

    if count % 2 == 0:
        return half_sq
    else:
        return (half_sq * (num % div)) % div
    

a,b,c = map(int, input().split())
print(multi(a, b, c))
