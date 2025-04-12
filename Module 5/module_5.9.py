# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 5.9 - Formative Test
# 9. Develop a program that prints the Fibonacci series up to 10 terms using a while loop.

terms = 10
a, b = 0, 1
count = 0

while count < terms:
    print(a)
    a, b = b, a + b
    count += 1