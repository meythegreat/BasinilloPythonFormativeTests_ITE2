# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 4.9 - Formative Test
# 9. Develop a program that determines if a given number is a prime number or not and prints the result.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")