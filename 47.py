# Question 47: Write a program to use the random module to generate five random integers.

import random

random_integers = [random.randint(1, 100) for _ in range(5)]
print("Five random integers between 1 and 100:")
print(random_integers)
