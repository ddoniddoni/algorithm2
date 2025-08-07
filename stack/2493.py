import sys
input = sys.stdin.readline

number = int(input())
array = list(map(int, input().split()))

temp = []
answer = []

for i in range(number):
    temp_num = array[i]
    while temp and temp[-1][1] <  temp_num:
        temp.pop()

    if temp:
        answer.append(temp[-1][0])
    else:
        answer.append(0)

    temp.append((i+1, temp_num))
    print(temp)

print(' '.join(map(str, answer)))
        




