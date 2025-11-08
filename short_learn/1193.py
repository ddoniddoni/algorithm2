import sys
input = sys.stdin.readline

X = int(input())

n = 1
while X > n * (n+1) // 2:
    n += 1

prev_sum = n * (n-1) // 2
pos = X - prev_sum
if n % 2 == 0:
    numerator = pos
    denominator = n - pos + 1

else:
    numerator = n - pos + 1
    denominator = pos

print(f"{numerator}/{denominator}")