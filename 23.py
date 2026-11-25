# Question 23: Write a function to calculate the average of a list of numbers.

def calculate_average(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

scores = [85, 90, 78, 92, 88]
print("Scores:", scores)
print(f"Average score: {calculate_average(scores):.2f}")
