import os
os.system('cls')

x = input("What would you like to know about? ")

print(x)
print("\nType: ", end=""); print(type(x))
print("\nDocString: ", end=""); print(x.__doc__)
print("\nAttribute List: ", end=""); print(dir(x))

if not help(x):
  help()
else:
  help(x)
