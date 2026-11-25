# Question 19: Write a function to check whether a string is a palindrome.

def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

test_strings = ["Madam", "Racecar", "Python", "A Santa at NASA"]
for s in test_strings:
    print(f"'{s}' is palindrome? -> {is_palindrome(s)}")
