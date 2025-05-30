total_price = int(input())
items = int(input())

for _ in range(items):
    A, B = map(int, input().split())
    total_price -= A * B

if total_price == 0:
    print('Yes')
else:
    print('No')