# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3.1 - Formative Test
# 1. Write a program that reads a string representing a floating-point number and converts it to an integer, then prints the integer value.

float_str = input("Enter a floating-point number: ")
try:
    float_num = float(float_str)
    int_num = int(float_num)
    print(f"The integer value is: {int_num}")
except ValueError:
    print("Invalid input. Please enter a valid floating-point number.")