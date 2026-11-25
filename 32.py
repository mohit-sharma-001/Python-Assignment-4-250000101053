# Question 32: Write a function to demonstrate variable-length arguments using *args.

def calculate_total(*args):
    print("Arguments received:", args)
    return sum(args)

print("Total (10, 20):", calculate_total(10, 20))
print("Total (1, 2, 3, 4, 5):", calculate_total(1, 2, 3, 4, 5))
