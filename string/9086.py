import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    text = input().strip()
    print(text[0] + text[len(text) - 1])    


