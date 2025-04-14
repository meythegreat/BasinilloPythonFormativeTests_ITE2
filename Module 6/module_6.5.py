# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 6 - Formative Test
# 5. Create a program that defines a tuple of temperatures in Celsius and prints the average temperature.

temperatures = (37, 40, 39, 42, 43, 38, 43, 41, 40, 39)
average_temperature = sum(temperatures) / len(temperatures)
print(f"Tuple of temperatures: {temperatures}")
print(f"Average temperature: {average_temperature:.1f}")