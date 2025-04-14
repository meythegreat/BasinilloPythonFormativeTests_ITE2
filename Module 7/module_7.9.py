# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 7 - Formative Test
# 9. Create a function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("hello"))