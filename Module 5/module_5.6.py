# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 5.6 - Formative Test
# 6. Develop a program that calculates the factorial of a given number using a for loop and prints the result.

number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}.")