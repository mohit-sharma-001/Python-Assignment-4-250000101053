# Question 20: Write a function to reverse a given string.

def reverse_string(s):
    return s[::-1]

original = "Hello World"
print("Original string:", original)
print("Reversed string:", reverse_string(original))
