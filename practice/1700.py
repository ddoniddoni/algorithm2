import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ele = list(map(int, input().split()))
plug = []
answer = 0

for i in range(K):

    if ele[i] in plug:
        continue

    if len(plug) < N:
        plug.append(ele[i])
        continue

    farthest = -1
    target = -1

    for p in plug:
        if p not in ele[i:]:
            target = p
            break
        else:
            idx = ele[i:].index(p)
            if idx > farthest:
                farthest = idx
                target = p
    
    plug.remove(target)
    plug.append(ele[i])
    answer += 1

print(answer)