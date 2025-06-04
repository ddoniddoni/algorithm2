import sys
input = sys.stdin.readline

count = int(input())
answer = ''
for _ in range(count):
    R,S = input().split()
    answer = ''
    for ch in S.strip():
        answer += ch * int(R)
    print(answer)