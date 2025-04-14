# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3 - Formative Test
# 1. Write a program that reads a string representing a floating-point number and converts it to an integer, then prints the integer value.

def convert_float_string_to_int():
    float_string = input("Enter a floating-point number as a string: ")
    print(f"Original string value: '{float_string}', Data type: {type(float_string)}")
    
    float_value = float(float_string)
    print(f"Converted float value: {float_value}, Data type: {type(float_value)}")
    
    int_value = int(float_value)
    print(f"Converted integer value: {int_value}, Data type: {type(int_value)}")

convert_float_string_to_int()
