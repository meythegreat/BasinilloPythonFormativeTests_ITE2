# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 4 - Formative Test
# 8. Create a program that checks if a given string is a palindrome or not and prints the result.

def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")