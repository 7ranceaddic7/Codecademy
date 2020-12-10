def sum_to_one(n):
  result = 1
  call_stack = []

  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED!")
  
  while call_stack:
    return_value = call_stack.pop()
    print(call_stack)
    print("Adding " + str(return_value["n_value"]) + " to result.")
    result += return_value["n_value"]

  return result, call_stack


print(sum_to_one(4))