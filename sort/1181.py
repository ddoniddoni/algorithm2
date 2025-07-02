import sys
input = sys.stdin.readline

count = int(input())
s_list = [input().strip() for _ in range(count)]
lists = list(set(s_list))
lists.sort()
lists.sort(key=len)

for word in lists:
    print(word)