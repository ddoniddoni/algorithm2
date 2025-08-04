import sys
input = sys.stdin.readline

n = int(input())
answer = []
for _ in range(n):
    command = input().split()
    action = command[0]

    if action == "push":
        answer.append(int(command[1]))

    elif action == "top":
        if not answer:
            print(-1)
        else:
            print(answer[-1])

    elif action == "size":
        print(len(answer))

    elif action == "empty":
        if not answer:
            print(1)
        else:
            print(0)

    elif action == "pop":
        if not answer:
            print(-1)
        else:
            print(answer.pop())