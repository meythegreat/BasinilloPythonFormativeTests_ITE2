# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 4 - Formative Test
# 5. Create a program that checks if a given character is a vowel or a consonant and prints the result.

char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"'{char}' is a vowel.")
elif char.isalpha():
    print(f"'{char}' is a consonant.")
else:
    print(f"'{char}' is not a letter. Please enter a letter.")