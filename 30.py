# Question 30: Write a function to demonstrate keyword arguments.

def student_info(name, age, course):
    print(f"Student: {name}, Age: {age}, Course: {course}")

# Arguments passed by explicit parameter name
student_info(course="Computer Science", name="Alice", age=20)
