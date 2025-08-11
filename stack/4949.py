import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == '.':
        break
    stack = []
    isBalanced = True

    for t in s:
        if t in '([':
            stack.append(t)
        elif t == ')':
            if not stack or stack[-1] != '(':
                isBalanced = False
                break
            stack.pop()
        elif t == ']':
            if not stack or stack[-1] != '[':
                isBalanced = False
                break
            stack.pop()
        
    if isBalanced and not stack:
        print('yes')
    else:
        print("no")  