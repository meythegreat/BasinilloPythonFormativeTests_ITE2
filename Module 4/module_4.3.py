# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 4 - Formative Test
# 3. Develop a program that determines if a given year is a leap year or not and prints the result.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")