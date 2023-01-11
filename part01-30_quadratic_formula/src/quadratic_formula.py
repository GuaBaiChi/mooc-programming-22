# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = float(input("Valuse of a: "))
b = float(input("Valuse of b: "))
c = float(input("Valuse of c: "))

# x = (-b ± sqrt(b²-4ac))/(2a)
#  so +-b

root1 = (-b + sqrt(b ** 2 - (4 * a * c))) / (2 * a)
root2 = (-b - sqrt(b ** 2 - (4 * a * c))) / (2 * a)

print(f"The roots are {root1} and {root2}")