import sys
input = sys.stdin.readline

words = [input().strip() for _ in range(5)]

result = ''
for i in range(15):  # 최대 길이 15
    for j in range(5):  # 5줄
        if i < len(words[j]):
            result += words[j][i]
print(result)