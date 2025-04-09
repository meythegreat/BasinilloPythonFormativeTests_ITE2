# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3.5 - Formative Test
# 5. Create a program that reads a string representing a boolean value ('1' for True, '0' for False), converts it to an integer data type (1 for True, 0 for False), and displays both the original string and the converted integer along with their data types.

boolean_string = input("Enter a boolean value as a string ('1' for True, '0' for False): ")
converted_integer = int(boolean_string)
print(f"Original string value: '{boolean_string}', Data type: {type(boolean_string)}")
print(f"Converted integer value: '{converted_integer}', Data type: {type(converted_integer)}")