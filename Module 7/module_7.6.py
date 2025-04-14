# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 7 - Formative Test
# 6. Create a function named calculate_average that takes a list of numbers as input and returns the average of those numbers.

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

numbers = [15, 30, 45, 60, 75, 90, 105]
print(calculate_average(numbers))