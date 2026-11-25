# Question 17: Write a function to calculate the factorial of a number.

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = 5
print(f"Factorial of {num} is: {factorial(num)}")
