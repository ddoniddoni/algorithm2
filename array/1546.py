import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

high_score = max(scores)

new_scores = [score / high_score * 100 for score in scores]
average = sum(new_scores) / n

print(average)