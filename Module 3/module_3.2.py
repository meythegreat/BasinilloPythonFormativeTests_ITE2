# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3 - Formative Test
# 2. Create a program that reads an integer, converts it to a string, and displays both the original integer and the converted string along with their data types.

def convert_int_to_string():
    integer_value = int(input("Enter an integer: "))
    print(f"Original integer value: {integer_value}, Data type: {type(integer_value)}")

    string_value = str(integer_value)
    print(f"Converted string value: '{string_value}', Data type: {type(string_value)}")

convert_int_to_string()