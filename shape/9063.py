import sys
input = sys.stdin.readline

count = int(input())

x_list = []
y_list = []

for _ in range(count):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

vertical = max(y_list) - min(y_list) 
horizon = max(x_list) - min(x_list)

print(vertical * horizon)