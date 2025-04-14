# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 8 - Formative Test
# 2. Create a class ElectricCar that inherits from the Car class. Add an additional attribute battery_size to the ElectricCar class. Create an object of the ElectricCar class and print its attributes.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

print(electric_car.make)
print(electric_car.model)
print(electric_car.year)
print(electric_car.battery_size)