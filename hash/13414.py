import sys
input = sys.stdin.readline

k, l = map(int, input().split())
students = {}


for i in range(l):
    s_id = input().strip()
    students[s_id] = i

final = sorted(students.items(), key=lambda x: x[1])
print(final)
for i in range(min(k, len(final))): print(final[i][0])