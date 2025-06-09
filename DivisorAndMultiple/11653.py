import sys
input = sys.stdin.readline

num = int(input())

if num == 1:
    pass
else:
    i = 2
    while i * i <= num:
        while num % i == 0:
            print(i)
            num //= i
        i +=1
    
    if num > 1:
        print(num)
