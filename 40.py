# Question 40: Write a program to demonstrate how local variables behave when two different functions use variables with the same name.

def func_one():
    val = 100
    print("func_one() -> val =", val)

def func_two():
    val = 999
    print("func_two() -> val =", val)

func_one()
func_two()
