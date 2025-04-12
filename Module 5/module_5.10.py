# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 5.10 - Formative Test
# 10. Write a program that prints numbers from 1 to 20 but stops when the number is divisible by 5 using a for loop.

for num in range(1, 21):
    if num % 5 == 0:
        break
    print(num)