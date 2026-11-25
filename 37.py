# Question 37: Write a program to demonstrate the use of global variables inside a function.

global_var = "Global Data (Accessible Everywhere)"

def read_global():
    print("Inside function, reading global_var:", global_var)

read_global()
print("Outside function, reading global_var:", global_var)
