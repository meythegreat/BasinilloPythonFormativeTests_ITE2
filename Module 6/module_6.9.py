# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 6.9 - Formative Test
# 9. Develop a program that defines a dictionary of car brands and their corresponding models, then prints each brand and its models.

car_brands = {
    "Toyota": ["Camry", "Corolla", "RAV4"],
    "Ford": ["Mustang", "F-150", "Explorer"],
    "Honda": ["Civic", "Accord", "CR-V"],
}

print("Car Brands and Models:")
for brand, models in car_brands.items():
    print(f"{brand}: {', '.join(models)}")