# Question 36: Write a program to demonstrate the use of local variables inside a function.

def demo_local_variable():
    local_msg = "I am a local variable inside demo_local_variable()"
    print(local_msg)

demo_local_variable()
# Accessing local_msg outside will result in NameError
# print(local_msg) # NameError: name 'local_msg' is not defined
