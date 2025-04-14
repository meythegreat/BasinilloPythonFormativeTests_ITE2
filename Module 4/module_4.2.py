# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 4 - Formative Test
# 2. Create a program that checks if a given number is positive, negative, or zero and prints the result.

number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")