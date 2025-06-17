import sys
input = sys.stdin.readline

num = int(input())
count = 0
n = 666

while True:
    if '666' in str(n):
        count += 1
        if count == num:
            print(n)
            break
    n += 1