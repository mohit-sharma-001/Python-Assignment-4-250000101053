# Question 28: Write a function to calculate simple interest using arguments and a return statement.

def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

p, r, t = 20000, 6.5, 2
interest = calculate_simple_interest(p, r, t)

print(f"Principal: {p}, Rate: {r}%, Time: {t} years")
print(f"Simple Interest: {interest}")
