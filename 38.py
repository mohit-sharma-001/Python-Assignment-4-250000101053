# Question 38: Write a program to demonstrate the difference between local and global variables having the same name.

x = "GLOBAL X"

def my_function():
    x = "LOCAL X"
    print("Inside my_function(): x =", x)

my_function()
print("Outside my_function(): x =", x)
