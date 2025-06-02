import sys
input = sys.stdin.readline

students = set(range(1,31))

submitted = set()

for _ in range(28):
    submitted.add(int(input()))

not_submitted = sorted(students - submitted)

for student in not_submitted:
    print(student)