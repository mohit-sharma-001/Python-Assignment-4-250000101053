# Question 35: Write a function that returns both the sum and product of two numbers.

def sum_and_product(x, y):
    return (x + y), (x * y)

a, b = 8, 5
total, prod = sum_and_product(a, b)

print(f"Numbers: {a}, {b}")
print(f"Sum    : {total}")
print(f"Product: {prod}")
