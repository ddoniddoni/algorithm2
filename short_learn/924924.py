def to_binary(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result

print(type(to_binary(10)))  # 1010
print(to_binary(0))   # 0