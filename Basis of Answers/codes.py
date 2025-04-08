# MODULE 2
# 1. Print Full Name
first_name = input("Enter First Name: ")
middle_name = input("Enter Middle Name (press Enter if none): ")
last_name = input("Enter Last Name: ")

# Print full name
if middle_name:
    print(f"{first_name} {middle_name[0]}. {last_name}")
else:
    print(f"{first_name} {last_name}")

# 2. Collect Personal Information
first_name = input("First Name: ")
middle_name = input("Middle Name (press Enter if none): ")
last_name = input("Last Name: ")
age = input("Age: ")
address = input("Address: ")
contact_number = input("Contact Number: ")
telephone_number = input("Telephone Number: ")
email = input("Email: ")

if middle_name:
    full_name = f"{first_name} {middle_name[0]}. {last_name}"
else:
    full_name = f"{first_name} {last_name}"

print(f"Hi, my name is {full_name}. I am {age} years old! I live in {address}. If you want to contact me, my contact number is {contact_number}, and my telephone number is {telephone_number}. You can reach me via email at {email}.")

# 3. Determine Relationship Status
status = input("Enter your relationship status (single/in a relationship): ")
if status.lower() == "in a relationship":
    print("Yes, I am in a relationship!")
else:
    print("No, I am single!")


# MODULE 3
# 1. Float to Integer
num = float(input("Enter a floating-point number: "))
print(int(num))

# 2. Integer to String
num = int(input("Enter an integer: "))
num_str = str(num)
print(f"Integer: {num} ({type(num)})")
print(f"String: {num_str} ({type(num_str)})")

# 3. String to Boolean
bool_str = input("Enter 'True' or 'False': ")
bool_val = bool_str == 'True'
print(f"Original: {bool_str} ({type(bool_str)})")
print(f"Boolean: {bool_val} ({type(bool_val)})")

# 4. String to Float
num_str = input("Enter a number: ")
num_float = float(num_str)
print(f"Original: {num_str} ({type(num_str)})")
print(f"Float: {num_float} ({type(num_float)})")

# 5. Boolean String to Integer
bool_str = input("Enter '1' for True or '0' for False: ")
bool_int = int(bool_str)
print(f"Original: {bool_str} ({type(bool_str)})")
print(f"Integer: {bool_int} ({type(bool_int)})")

# 6. String Length
s = input("Enter a string: ")
print(len(s))

# 7. String Uppercase
s = input("Enter a string: ")
print(s.upper())

# 8. Concatenate Strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(s1 + s2)

# 9. Reverse String
s = input("Enter a string: ")
print(s[::-1])

# 10. Count Vowels
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print(count)


# MODULE 4
# 1. Even or Odd
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")

# 2. Positive, Negative, or Zero
n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 3. Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 4. Largest of Three
nums = [int(input("Enter a number: ")) for _ in range(3)]
print(max(nums))

# 5. Vowel or Consonant
ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 6. String Empty or Not
s = input("Enter a string: ")
print("Empty" if not s else "Not empty")

# 7. Divisible by 5 and 7
n = int(input("Enter a number: "))
print("Divisible by both 5 and 7" if n % 5 == 0 and n % 7 == 0 else "Not divisible")

# 8. Palindrome
s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not a palindrome")

# 9. Prime Number
n = int(input("Enter a number: "))
if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)):
    print("Prime")
else:
    print("Not prime")

# 10. Sum from 1 to n
n = int(input("Enter a number: "))
print(sum(range(1, n+1)))


# MODULE 5
# 1. 1 to 5 (While Loop)
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. Even Numbers (For Loop)
for i in range(2, 11, 2):
    print(i)

# 3. Sum 1 to 10 (While Loop)
i, total = 1, 0
while i <= 10:
    total += i
    i += 1
print(total)

# 4. Every Third Number (For Loop)
for i in range(3, 16, 3):
    print(i)

# 5. Reverse 10 to 1 (While Loop)
i = 10
while i >= 1:
    print(i)
    i -= 1

# 6. Factorial (For Loop)
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)

# 7. Skip 5 (While Loop)
i = 1
while i <= 10:
    if i != 5:
        print(i)
    i += 1

# 8. Multiplication Table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 9. Fibonacci (While Loop)
a, b, count = 0, 1, 0
while count < 10:
    print(a)
    a, b = b, a + b
    count += 1

# 10. Stop at Divisible by 5 (For Loop)
for i in range(1, 21):
    if i % 5 == 0:
        break
    print(i)


# MODULE 6
# 1. List of Fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. Tuple of Colors
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# 3. Dictionary of Students
students = {"Juan": 20, "Ana": 21}
for name, age in students.items():
    print(f"{name}: {age}")

# 4. Sum of Numbers
numbers = [1, 2, 3, 4]
print(sum(numbers))

# 5. Average Temperature
temps = (30, 32, 28, 35)
print(sum(temps)/len(temps))

# 6. Dictionary of Books
books = {"1984": "Orwell", "Noli Me Tangere": "Rizal"}
for title, author in books.items():
    print(f"{title} by {author}")

# 7. Sorted Cities
cities = ["Manila", "Cebu", "Davao"]
cities.sort()
print(cities)

# 8. Min and Max Ages
ages = (18, 22, 20)
print(min(ages), max(ages))

# 9. Dictionary of Cars
cars = {"Toyota": "Corolla", "Honda": "Civic"}
for brand, model in cars.items():
    print(f"{brand}: {model}")

# 10. Total Price with Discount
prices = [100, 200, 300]
total = sum(prices) * 0.9
print(total)


# MODULE 7
# 1. List of Integers
nums = [1, 2, 3, 4]
for num in nums:
    print(num)

# 2. List of Strings Reversed
strings = ["hello", "world"]
for s in strings:
    print(s[::-1])

# 3. Sum of Numbers in List
nums = [1, 2, 3]
print(sum(nums))

# 4. Search Student
students = ["Juan", "Ana"]
name = input("Enter student name: ")
if name in students:
    print("Student found")
else:
    print("Student not found")

# 5. Greet Function
def greet(name):
    print(f"Hello, {name}!")

greet("Juan")

# 6. Calculate Average
def calculate_average(numbers):
    return sum(numbers)/len(numbers)

print(calculate_average([1, 2, 3, 4]))

# 7. Is Odd
def is_odd(n):
    return n % 2 != 0

print(is_odd(3))

# 8. Reverse String
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

# 9. Count Vowels
def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels("hello"))

# 10. Find Max
def find_max(numbers):
    return max(numbers)

print(find_max([1, 2, 3, 4]))


# MODULE 8
# 1. Car Class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Toyota", "Corolla", 2020)
print(car.make, car.model, car.year)

# 2. Electric Car Class
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

ecar = ElectricCar("Tesla", "Model S", 2022, 100)
print(ecar.make, ecar.model, ecar.year, ecar.battery_size)

# 3. MyRange Iterator
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            val = self.start
            self.start += 1
            return val
        else:
            raise StopIteration

for num in MyRange(1, 5):
    print(num)

# 4. Book and Library Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

library = Library()
library.add_book(Book("1984", "George Orwell"))
library.display_books()

# 5. Vehicle Class with Inheritance
class Vehicle:
    def drive(self):
        return "Driving a vehicle"

class Car(Vehicle):
    def drive(self):
        return "Driving car"

class Motorcycle(Vehicle):
    def drive(self):
        return "Driving motorcycle"

car = Car()
motorcycle = Motorcycle()
print(car.drive())
print(motorcycle.drive())
