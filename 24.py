# Question 24: Write a function to count vowels in a given string.

def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)

text = "Artificial Intelligence and Machine Learning"
print(f"Text: '{text}'")
print("Total vowels:", count_vowels(text))
