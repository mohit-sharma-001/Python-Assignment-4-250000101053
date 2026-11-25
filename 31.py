# Question 31: Write a function to demonstrate default arguments.

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Using default greeting
greet_user("Alice")

# Overriding default greeting
greet_user("Bob", "Good morning")
