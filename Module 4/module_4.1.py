# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 4.1 - Formative Test
# 1. Write a program that checks if a given number is even or odd and prints the result.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")