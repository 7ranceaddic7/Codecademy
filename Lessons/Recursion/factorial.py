def factorial(n):
  if n == 1:
    print("Factorial Complete!")
    return n
  else:
    return n * factorial(n-1)

print(factorial(998))