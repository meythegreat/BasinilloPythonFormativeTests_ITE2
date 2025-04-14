# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 7.3  - Formative Test
# 3. Develop a program that reads a list of numbers and calculates the sum of all numbers in the list, then prints the sum.

numbers = input("Enter a list of numbers separated by spaces: ")
number_list = map(int, numbers.split())
total_sum = sum(number_list)
print("Sum of all numbers:", total_sum)