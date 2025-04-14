# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3 - Formative Test
# 4. Write a program that reads a string representing a number (integer or float), converts it to a float, and displays both the original string and the converted float along with their data types.

number_string = input("Enter a number as a string: ")
converted_float = float(number_string)
print(f"Original string value: '{number_string}', Data type: {type(number_string)}")
print(f"Converted float value: '{converted_float}, Data type: {type(converted_float)}")