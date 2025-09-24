import sys
input = sys.stdin.readline

word = input().strip()
answer = 0
stack = []
temp = 1
for i in range(len(word)):
    ch = word[i]

    if ch == '(':
        stack.append(ch)
        temp *= 2
    elif ch == '[':
        stack.append(ch)
        temp *= 3
    elif ch == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if word[i-1] == '(':
            answer += temp
        stack.pop()
        temp //= 2
    elif ch == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if word[i-1] == '[':
            answer += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)

   

    