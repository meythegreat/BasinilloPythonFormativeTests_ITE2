# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3.2 - Formative Test
# 2. Create a program that reads an integer, converts it to a string, and displays both the original integer and the converted string along with their data types.

num = int(input("Enter an integer: "))
num_str = str(num)
print(f"Integer: {num} ({type(num)})")
print(f"String: {num_str} ({type(num_str)})")