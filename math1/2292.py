import sys
input = sys.stdin.readline

count = int(input())

if count == 1:
    print(1)
else:
    layer = 1
    while 3 * layer * layer - 3 * layer + 1 < count:
        layer += 1
    print(layer)

