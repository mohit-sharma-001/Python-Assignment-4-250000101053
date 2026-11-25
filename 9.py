# Question 9: Write a program to calculate the value of sine, cosine and tangent for a given angle.

import math

angle_degrees = 45.0
angle_radians = math.radians(angle_degrees)

sin_val = math.sin(angle_radians)
cos_val = math.cos(angle_radians)
tan_val = math.tan(angle_radians)

print(f"Angle: {angle_degrees} degrees ({angle_radians:.4f} radians)")
print(f"sin({angle_degrees}°) = {sin_val:.4f}")
print(f"cos({angle_degrees}°) = {cos_val:.4f}")
print(f"tan({angle_degrees}°) = {tan_val:.4f}")
