# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(numberA, numberB, limit):
    answer = [0] * 1001

    for i in range(1, limit // numberA + 1):
        answer[i * numberA] = 1
    for i in range(1, limit // numberB + 1):
        answer[i * numberB] = 1

    for i in range(1, limit // numberA + 1):
        for j in range(1, limit // numberB + 1):
            val = i * numberA + j * numberB
            if val <= limit:
                answer[val] = 1

    return sum(answer[1:])

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 
numberA1 = 2
numberB1 = 4
limit1 = 10
ret1 = solution(numberA1, numberB1, limit1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

numberA2 = 2
numberB2 = 3
limit2 = 10
ret2 = solution(numberA2, numberB2, limit2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")