# Question 15: Write a function to check whether a number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

for test_val in [12, 17, 0, -5]:
    print(f"{test_val} is {check_even_odd(test_val)}")
