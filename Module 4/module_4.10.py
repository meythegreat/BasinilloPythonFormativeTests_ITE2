# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 4 - Formative Test
# 10. Write a program that calculates the sum of all the numbers from 1 to a given number.

number = int(input("Enter a number: "))
total_sum = sum(range(1, number + 1))
print(f"The sum of numbers from 1 to {number} is {total_sum}.")