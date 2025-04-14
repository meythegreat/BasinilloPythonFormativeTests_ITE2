# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 8 - Formative Test
# Define a class Vehicle with a method drive() that returns a generic driving message. Create two subclasses Car and Motorcycle that inherit from Vehicle and override the drive() method to return "Driving car" and "Driving motorcycle" respectively.

class Vehicle:
    def drive(self):
        return "Generic driving message"

class Car(Vehicle):
    def drive(self):
        return "Driving car"

class Motorcycle(Vehicle):
    def drive(self):
        return "Driving motorcycle"

vehicle = Vehicle()
print(vehicle.drive())

car = Car()
print(car.drive())

motorcycle = Motorcycle()
print(motorcycle.drive())