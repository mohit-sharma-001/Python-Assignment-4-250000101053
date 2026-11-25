# Question 13: Write a function to calculate the area of a circle.

import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

r = 5.0
area = calculate_circle_area(r)
print(f"Radius: {r}")
print(f"Area of circle: {area:.4f}")
