# # recursion call
# def factorial(n):
#     if n < 0:
#         return "Number less than zero, try again."
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)

# # iterative call
# def factorial(n):
#     if n < 0:
#         return "Number less than zero, try again."
#     result = 1
#     while n != 0:
#         result *= n
#         n -= 1
#     return result

# test cases
print(factorial(1) == 1)
print(factorial(3) == 6)
# 1 * 2 * 3 = 6
print(factorial(0) == 1)
print(factorial(5) == 120)
# 1 * 2 * 3 * 4 * 5 = 120
