# Question 14: Write a function to find the square and cube of a given number.

def square_and_cube(n):
    return n ** 2, n ** 3

num = 4
sq, cb = square_and_cube(num)
print(f"Number: {num}")
print(f"Square: {sq}")
print(f"Cube  : {cb}")
