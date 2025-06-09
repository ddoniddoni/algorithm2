import sys
input = sys.stdin.readline

while True:
    num = int(input())
    
    if num == -1:
        break
    answer = ""
    temp = 0
    for i in range(1, (num // 2) + 1):
        if i == 1:
            answer += "1"
            temp += i
        else:
            if num % i == 0:
                answer += (" + " + str(i))
                temp += i

    if temp == num:
        print(f"{num} = " + answer)
    else:
        print(f"{num} is NOT perfect.")    

