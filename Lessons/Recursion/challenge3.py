# # iterative call
# Linear - O(N), where "N" is the number of digits in the number
# def sum_digits(n):
#   if n < 0:
#     n = abs(n)
#   result = 0
#   while n != 0:
#     result += n % 10
#     n = n // 10
#   return result + n


# # recursive call
# def sum_digits(n):
#   if abs(n) <= 9:
#     return abs(n)
#   last_digit = abs(n) % 10
#   return last_digit + sum_digits(abs(n) // 10)

# test cases
print(sum_digits(12) == 3)
# 1 + 2 = 3
print(sum_digits(552) == 12)
# 5 + 5 + 2 = 12
print(sum_digits(123456789) == 45)
# 1 + 2 + 3 + 4... = 45
print(sum_digits(-123456789) == 45)