# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 2.2 - Formative Test
# 2. Python Program to Collect Personal Information
# ▪ Write a Python program that allows the user to input their personal information, including first name, middle name, last name, age, address, contact number, telephone number, and email.
# ▪ Construct a sentence using the provided information to create a brief introduction.

first_name = input("First Name: ")
middle_name = input("Middle Name (press Enter if none): ")
last_name = input("Last Name: ")
age = input("Age: ")
address = input("Address: ")
contact_number = input("Contact Number: ")
telephone_number = input("Telephone Number: ")
email = input("Email: ")

if middle_name:
    full_name = f"{first_name} {middle_name[0]}. {last_name}"
else:
    full_name = f"{first_name} {last_name}"

print(f"Hi, my name is {full_name}. I am {age} years old! I live in {address}. If you want to contact me, my contact number is {contact_number}, and my telephone number is {telephone_number}. You can reach me via email at {email}.")