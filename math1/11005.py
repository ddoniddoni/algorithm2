import sys
input = sys.stdin.readline

a,b = map(int, input().split())
result = ""

if a == 0:
    result = ""

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while a > 0:
    result = digits[a % b] + result
    a //= b

print(result)


