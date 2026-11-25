# Question 39: Write a program to modify a global variable inside a function using the global keyword.

counter = 0

def increment():
    global counter
    counter += 1
    print("Inside function, counter =", counter)

print("Before calls, counter =", counter)
increment()
increment()
increment()
print("After calls, counter =", counter)
