# Question 41: Write a Python program to create a user-defined module containing a function to calculate the square of a number and import it into another program.

# Demonstrating creation and dynamic import of a user module
import types

# Create module code
module_code = """
def calculate_square(num):
    return num ** 2
"""

# Compile and execute into a module namespace
my_module = types.ModuleType("square_module")
exec(module_code, my_module.__dict__)

# Using the imported function from the module
result = my_module.calculate_square(9)
print("Square calculated using user-defined module:", result)
