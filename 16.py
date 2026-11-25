# Question 16: Write a function to find the greatest among three numbers.

def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x, y, z = 45, 89, 72
print(f"Numbers: {x}, {y}, {z}")
print("Greatest number is:", find_greatest(x, y, z))
