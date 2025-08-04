import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

stack = []
answer = []
current_num = 1

for num in array:
    while current_num <= num:
        stack.append(current_num)
        answer.append('+')
        current_num += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        exit()

for op in answer:
    print(op)

