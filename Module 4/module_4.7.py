# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 4.7 - Formative Test
# 7. Write a program that checks if a given number is divisible by both 5 and 7 and prints the result.

number = int(input("Enter a number: "))
if number % 5 == 0 and number % 7 == 0:
    print(f"{number} is divisible by both 5 and 7.")
else:
    print(f"{number} is not divisible by both 5 and 7.")