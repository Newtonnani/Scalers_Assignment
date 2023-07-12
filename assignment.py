class Manufacturer:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.brands = []

    def add_brand(self, brand):
        self.brands.append(brand)

    def get_brands(self):
        return self.brands

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

        



        
        
# Demonstration
# Create two manufacturer objects
manufacturer1 = Manufacturer("Manufacturer 1", "Location 1")
manufacturer2 = Manufacturer("Manufacturer 2", "Location 2")

# Add different brands of cars to each manufacturer
manufacturer1.add_brand("Brand 1")
manufacturer1.add_brand("Brand 2")
manufacturer2.add_brand("Brand 3")
manufacturer2.add_brand("Brand 4")

# Getting all brands
print("Manufacturer 1 all brands", manufacturer1.get_brands())
print("Manufacturer 2 all brands", manufacturer2.get_brands())

# Create multiple car objects for each manufacturer
car1 = Car("Brand 1", "Model 1", 2022)
car2 = Car("Brand 1", "Model 2", 2023)
car3 = Car("Brand 2", "Model 3", 2021)
car4 = Car("Brand 3", "Model 4", 2023)
car5 = Car("Brand 3", "Model 5", 2022)
car6 = Car("Brand 4", "Model 6", 2021)

# Print the details of the cars
print("Car details:")
car1.get_details()
car2.get_details()
car3.get_details()
car4.get_details()
car5.get_details()
car6.get_details()
