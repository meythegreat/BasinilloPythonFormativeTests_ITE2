# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 7 - Formative Test
# 2. Create a program that defines a list of strings and prints each string in reverse order.

strings = ['Vice Ganda', 'Vhong Navarro', 'Karylle', 'Jhong Hilario', 'Billy Crawford']
reversed_strings = [string[::-1] for string in strings]
print("List of  strings: " + str(strings))  
print("Reversed strings: " + str(reversed_strings))