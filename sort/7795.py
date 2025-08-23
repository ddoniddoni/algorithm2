import sys
input = sys.stdin.readline

n = int(input())


for _ in range(n):
    count = 0
    n, m = map(int, input().split())
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    num1.sort()
    num2.sort()
    
    j = 0
    for n1 in num1:
        while j < m and num2[j] < n1:
            j += 1
        count += j
    print(count)