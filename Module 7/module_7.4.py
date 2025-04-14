# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 7.4  - Formative Test
# 4. Create a program that defines a list of student names and allows the user to search for a student by entering their name. If the student is found, print "Student found", otherwise print "Student not found".

students = ["Stanley", "Ephraim", "Carl", "Ephraim", "Erlyn", "Stephanie", "Erika", "Analyn", "Jenny"]

search_name = input("Enter a student name to search: ")

if search_name in students:
    print("Student found")
else:
    print("Student not found")