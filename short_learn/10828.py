import sys
input = sys.stdin.readline

n = int(input())
answer = []
for _ in range(n):
    orders = input().split()
    if orders[0] == 'push':
        answer.append(orders[1])
    
    elif orders[0] == 'top':
        if answer:
            print(answer[-1])
        else:
            print(-1)
    
    elif orders[0] == 'size':
        print(len(answer))
    elif orders[0] == 'empty':
        if answer:
            print(0)
        else:
            print(1)
    elif orders[0] == 'pop':
        if not answer:
            print(-1)
        else:
            print(answer.pop())