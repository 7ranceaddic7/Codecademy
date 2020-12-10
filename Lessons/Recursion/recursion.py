def sum_to_one(n):
  if n == 1:
    print("Recursing final input: {0}".format(n))
    return n
  else:
    print("Recursing with input: {0}".format(n))
    return sum_to_one(n-1) + n

print(sum_to_one(7))