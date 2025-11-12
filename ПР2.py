import math
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))
s = ((9 + (x - y)**2) ** (1/3)) / (x**2 + y**2 + 2) - math.exp(abs(x - y)) * (math.tan(z))**3
print(f"s = {s:.5f}")