# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3.1 - Formative Test
# 1. Write a program that reads a string representing a floating-point number and converts it to an integer, then prints the integer value.

# Function to convert a string representing a floating-point number to an integer
def convert_float_string_to_int():
    # Read input from the user
    float_string = input("Enter a floating-point number as a string: ")
    
    # Print the original string and its type
    print(f"Original string value: '{float_string}', Data type: {type(float_string)}")
    
    # Convert the string to a float
    float_value = float(float_string)
    
    # Print the converted float and its type
    print(f"Converted float value: {float_value}, Data type: {type(float_value)}")
    
    # Convert the float to an integer
    int_value = int(float_value)
    
    # Print the final integer value
    print(f"Converted integer value: {int_value}, Data type: {type(int_value)}")

# Call the function
convert_float_string_to_int()