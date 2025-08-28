import sys
input = sys.stdin.readline

n = int(input())

flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append((start, end))

flowers.sort(key=lambda x: (x[0], x[1]))

cur = 301
end = 1130

idx = 0
count = 0
max_end = 0

while cur <= end:
    found = False
    while idx < n and flowers[idx][0] <= cur:
        max_end = max(max_end, flowers[idx][1])
        idx += 1
        found = True
    
    if not found:
        print(0)
        exit()

    count += 1
    cur = max_end
    if cur > end:
        break
print(count)

