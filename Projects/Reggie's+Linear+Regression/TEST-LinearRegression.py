x = x_point = 0
y = y_point = 0
m = b = 0

## get_y
def get_y(m, b, x):
  global y
  print("GET_Y values in are: M: " + str(m) + ", B: " + str(b) + ", X: " + str(x))
  y = m*x+b
  print("GET_Y values out are Y: " + str(y))
  return y


# ## calculate_error(), take  m, b, point (x, y) 
# ## return the distance between the line and the point.
def calculate_error(m, b, point):
  dist = 0
  x = x_point = point[0]
  y = y_point = point[1]

  get_y(m, b, x)
  dist = abs(y - y_point)
  return dist


# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
print("\n")

# the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
print("\n")

# the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
print("\n")

# the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))
print("\n")
