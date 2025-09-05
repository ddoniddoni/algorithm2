def solution(N, info, game):
    # 전략을 아는 사람 집합
    know = set(info[1])
    result = 0

    for g in game:
        # 이번 게임에 전략을 아는 사람이 있는지 확인
        if any(player in know for player in g):
            continue  # B가 짐
        else:
            result += 1  # B가 이김
            # 이제 이 사람들도 전략을 알게 됨
            know.update(g)

    return result


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
N = 5
info = [[ 1 ], [ 4 ]]
game = [[1, 2], [3], [3, 4]]
ret = solution(N, info, game)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

N = 7
info = [[ 3 ], [ 1, 2, 3 ]]
game = [[1], [2], [3], [4], [5], [6], [4, 5], [3, 6]]
ret = solution(N, info, game)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")