# Question 8: Write a program to calculate the GCD and LCM of two numbers using mathematical functions.

import math

a = 36
b = 60

gcd = math.gcd(a, b)
# LCM(a, b) = abs(a * b) // GCD(a, b) or math.lcm in Python 3.9+
lcm = math.lcm(a, b) if hasattr(math, 'lcm') else abs(a * b) // gcd

print(f"Numbers: a = {a}, b = {b}")
print(f"GCD (Greatest Common Divisor): {gcd}")
print(f"LCM (Least Common Multiple)  : {lcm}")
