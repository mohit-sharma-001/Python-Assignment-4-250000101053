# Question 22: Write a function to find the largest element in a list.

def find_largest(lst):
    if not lst:
        return None
    largest = lst[0]
    for x in lst[1:]:
        if x > largest:
            largest = x
    return largest

data = [34, 12, 89, 5, 92, 45]
print("List:", data)
print("Largest element:", find_largest(data))
