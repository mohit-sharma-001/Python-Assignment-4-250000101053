# Question 4: Write a program to demonstrate type conversion using int(), float() and str().

s_num = "120"
s_flt = "45.67"
i_num = 50

converted_int = int(s_num)
converted_flt = float(s_flt)
converted_str = str(i_num)

print(f"int('{s_num}')   : {converted_int} ({type(converted_int).__name__})")
print(f"float('{s_flt}') : {converted_flt} ({type(converted_flt).__name__})")
print(f"str({i_num})      : '{converted_str}' ({type(converted_str).__name__})")
