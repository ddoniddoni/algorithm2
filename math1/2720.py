import sys
input = sys.stdin.readline

count = int(input())

for _ in range(count):
    price = int(input())

    quarter = price // 25
    price %= 25

    dime = price // 10
    price %= 10

    nickel = price // 5
    price %= 5

    penny = price // 1

    print(quarter, dime, nickel, penny)

