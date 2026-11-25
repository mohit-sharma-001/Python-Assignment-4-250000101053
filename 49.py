# Question 49: Write a program to create a user-defined module for student marks calculation and use it in another Python program.

import types

marks_module_code = """
def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks, max_marks_per_subject=100):
    return (sum(marks) / (len(marks) * max_marks_per_subject)) * 100

def get_result(percentage):
    return "Pass" if percentage >= 40 else "Fail"
"""

marks_calc = types.ModuleType("marks_calc")
exec(marks_module_code, marks_calc.__dict__)

student_marks = [75, 82, 68, 91, 88]
total = marks_calc.calculate_total(student_marks)
perc = marks_calc.calculate_percentage(student_marks)
status = marks_calc.get_result(perc)

print("Student Marks:", student_marks)
print(f"Total: {total}")
print(f"Percentage: {perc:.2f}%")
print(f"Status: {status}")
