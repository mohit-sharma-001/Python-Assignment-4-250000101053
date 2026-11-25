# Question 33: Write a function that accepts a list as an argument and returns its largest element.

def get_max_from_list(items):
    return max(items)

numbers = [100, 250, 45, 780, 320]
print("List:", numbers)
print("Largest element:", get_max_from_list(numbers))
