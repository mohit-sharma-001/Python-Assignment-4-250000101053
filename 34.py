# Question 34: Write a function that accepts a string and returns the number of uppercase and lowercase characters.

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

sample_text = "Hello World, Welcome to PYTHON!"
u, l = count_case(sample_text)

print(f"Text: '{sample_text}'")
print(f"Uppercase: {u}, Lowercase: {l}")
