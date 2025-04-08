# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 2.1
# 1. Python Program to Print Full Name
# ▪  Develop a Python program that prompts the user to input their first name, middle name (if any), and last name.
# ▪ Print the full name of the person. If the person doesn't have a middle name, print only the first name and last name.
# ▪ Add comments in the code for documentation purposes.

first_name = input("Enter First Name: ")
middle_name = input("Enter Middle Name (press Enter if none): ")
last_name = input("Enter Last Name: ")

if middle_name:
    print(f"{first_name} {middle_name[0]}. {last_name}")
else:
    print(f"{first_name} {last_name}")