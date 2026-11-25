# Question 50: Write a program to create a simple user-defined package containing two modules and import functions from both modules.

import types

# Module 1: string utilities
mod1_code = """
def to_title(text): return text.title()
"""
mod1 = types.ModuleType("str_utils")
exec(mod1_code, mod1.__dict__)

# Module 2: math utilities
mod2_code = """
def cube(n): return n ** 3
"""
mod2 = types.ModuleType("num_utils")
exec(mod2_code, mod2.__dict__)

# Simulated package
class MyPackage:
    str_utils = mod1
    num_utils = mod2

pkg = MyPackage()

print("Using package.str_utils.to_title():", pkg.str_utils.to_title("hello world from package"))
print("Using package.num_utils.cube(4)   :", pkg.num_utils.cube(4))
