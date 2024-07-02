# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?
x = 3
x = float(x)
print(type(x))

x = 3.0
x = int(x)
print(type(x))

x = 9.5 / 2
print(x)

x, y = 2, 5
print(x * y)
