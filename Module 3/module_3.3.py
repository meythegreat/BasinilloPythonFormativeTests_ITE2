# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3 - Formative Test
# Develop a program that reads a boolean value as a string ('True' or 'False'), converts it to a boolean data type, and displays both the original string and the converted boolean along with their data types.

input_str = input("Enter a boolean value as a string ('True' or 'False'): ")
converted_bool = input_str == 'True'
print(f"Original string value: '{input_str}', Data type: {type(input_str)}")
print(f"Converted boolean value: {converted_bool}, Data type: {type(converted_bool)}")