# Question 42: Write a program to create a module containing functions for addition, subtraction, multiplication and division.

import types

arithmetic_code = """
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else 'Division by zero'
"""

calc = types.ModuleType("calculator_module")
exec(arithmetic_code, calc.__dict__)

print("Addition (10 + 5)      :", calc.add(10, 5))
print("Subtraction (10 - 5)   :", calc.subtract(10, 5))
print("Multiplication (10 * 5):", calc.multiply(10, 5))
print("Division (10 / 5)      :", calc.divide(10, 5))
