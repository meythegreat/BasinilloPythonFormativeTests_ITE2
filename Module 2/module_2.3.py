# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 2.3 - Formative Test
# 3. Python Program to Determine Relationship Status
# ▪ Develop a Python program that prompts the user to indicate their relationship status (single or in a relationship).
# ▪ Based on the user's response, provide an appropriate output.

status = input("Enter your relationship status (single/in a relationship): ")
if status.lower() == "in a relationship":
    print("Yes, I am in a relationship!")
else:
    print("No, I am single!")