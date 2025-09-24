import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))
max_ret = float('-inf')
min_ret = float('inf')
def apply_cal(a, b, cal_index):
    if cal_index == 0:
        return a + b
    elif cal_index == 1:
        return a - b
    elif cal_index == 2:
        return a * b
    else:
        if a < 0:
            return - (abs(a) // b)
        else:
            return a // b

def dfs(curr, idx):
    global max_ret, min_ret
    if idx == n:
        max_ret = max(max_ret, curr)
        min_ret = min(min_ret, curr)
        return
    
    for i in range(4):
        if cal[i] > 0:
            cal[i] -= 1
            next_val = apply_cal(curr, numbers[idx], i)
            dfs(next_val, idx+1)
            cal[i] += 1

dfs(numbers[0], 1)
print(max_ret)
print(min_ret)