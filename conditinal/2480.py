x, y, z = map(int, input().split())
reward = 0

if x == y == z:
    reward = 10000 + (x * 1000)
elif x == y or y == z or x == z:
    if x == y:
        reward = 1000 + x * 100
    elif y == z:
        reward = 1000 + y * 100
    else:
        reward = 1000 + z * 100
else:
    reward = max(x,y,z) * 100

print(reward)