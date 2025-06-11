import sys
input = sys.stdin.readline

array = []
x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in x_list:
    if x_list.count(i) == 1:
        answerX = i

for i in y_list:
    if y_list.count(i) == 1:
        answerY = i

print(answerX, answerY)