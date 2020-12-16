# # recursive call
# def fibonacci(n):
#   if n < 0:
#     return -(fibonacci(abs(n) - 1) + fibonacci(abs(n) -2)
#   if n <= 1:
#     return n
#   return fibonacci(n - 1) + fibonacci(n -2)


# # iterative call
# def fibonacci(n):
#   if n < 0:
#     ValueError("Input 0 or greater only!")

#   fibs = [0, 1]
  
#   if n <= len(fibs) - 1:
#     return fibs[n]

#   while n > len(fibs) - 1:
#     fibs.append(fibs[-1] + fibs[-2])
    
#   return fibs[-1]

# # MY iterative call to work on
# def fibonacci(n):
#   if n < 0:
#     ValueError("Input 0 or greater only!")

#   if n == 0:
#     return 0

#   while (n != 0, -1):
#     return (n-1) + (n-2)


# test cases
print(fibonacci(3) == 2)
# 2 + 1 = 3
print(fibonacci(7) == 13)
# 7 + 6 = 13
# print(fibonacci(-7) == -13)
# -7 + -6 = -13
print(fibonacci(0) == 0)