# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 5 - Formative Test
# 8. Create a program that prints the multiplication table of a given number using a for loop.

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
