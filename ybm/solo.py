# def sum_list(numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total

# print(sum_list([1,2,3,4]))

# def reverse_string(s):
#     result = ""
#     for i in range(len(s)):
#         result += s[-i]
#     return result

# print(reverse_string("hello"))

# def is_palindrome(s: str) -> bool:
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
    


# print(is_palindrome("level"))   # True
# print(is_palindrome("pythonnohtyp"))  # False

# def find_max(numbers):
#     max_val = numbers[0]
#     for n in numbers:
#         if n > max_val:
#             max_val = n
#     return max_val

# print(find_max([3, 8, 2, 5]))  # 출력: 8

# def count_vowels(s):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for ch in s:
#         if ch in vowels:
#             count += 1   # 오류 있음
#     return count

# print(count_vowels("banana"))  # 기대 출력: 3

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]