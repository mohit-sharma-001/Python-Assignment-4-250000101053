# Question 25: Write a function to find the length of a string without using the len() function.

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

text = "Uttarakhand Technical University"
print(f"String: '{text}'")
print("Length (without len()):", string_length(text))
