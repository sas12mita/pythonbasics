import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# discriminant
d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Two real roots:", x1, x2)

elif d == 0:
    x = -b / (2*a)
    print("One real root:", x)

else:
    print("No real roots (complex roots)")