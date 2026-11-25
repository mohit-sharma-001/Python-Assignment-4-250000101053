# Question 48: Write a program to use the math module to calculate the value of a mathematical expression.

import math

# Expression: (sqrt(a^2 + b^2) + log(x)) / (sin(theta) + cos(theta))
a = 3
b = 4
x = 10
theta = math.radians(30)

hypot = math.sqrt(a**2 + b**2)
log_val = math.log10(x)
trig_sum = math.sin(theta) + math.cos(theta)

expression_result = (hypot + log_val) / trig_sum

print(f"Expression result: {expression_result:.4f}")
