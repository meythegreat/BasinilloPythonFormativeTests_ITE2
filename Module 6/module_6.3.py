# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 6.3 - Formative Test
# 3. Develop a program that creates a dictionary of student names and their corresponding ages, then prints each student name and age.

students = {'Erlyn': 20, 'Carl': 20, 'Stanley': 19, 'Stephanie': 19, 'Ephraim': 20, 'Erika': 20}
for name, age in students.items():
    print(f"{name}: {age}")