# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 7 - Formative Test
# 10. Develop a function named find_max that takes a list of numbers as input and returns the maximum number in the list.

def find_max(numbers):
    return max(numbers) if numbers else None

numbers = [10, 20, 5, 35, 15]
print(find_max(numbers))