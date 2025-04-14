# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 3 - Formative Test
# 10. Create a program that reads a string and counts the number of vowels (a, e, i, o, u) in it.

string_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string_input if char in vowels)
print(f"The number of vowels in the string is: {count}")