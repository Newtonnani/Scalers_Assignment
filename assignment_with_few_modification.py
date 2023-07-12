class Manufacturer:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars_by_brand = {}
        self.brands = []

    def add_brand(self, brand):
        self.brands.append(brand)

    def get_brands(self):
        return self.brands

    def add_car(self, car):
        brand = car.get_brand()
        chassis_number = car.get_chassis()

        if brand not in self.cars_by_brand:
            self.cars_by_brand[brand] = {}

        self.cars_by_brand[brand][chassis_number] = car

    def get_car_by_brand_and_chassis(self, brand, chassis_number):
        if brand in self.cars_by_brand and chassis_number in self.cars_by_brand[brand]:
            return self.cars_by_brand[brand][chassis_number]
        else:
            return None


class Car:
    def __init__(self, brand, model, chassis, year):
        self.brand = brand
        self.model = model
        self.chassis = chassis
        self.year = year

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_chassis(self):
        return self.chassis

    def get_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Chassis: {self.chassis}")



# brand x has car y chasis z  -- > O(1)

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
car1 = Car("Brand 1", "Model 1", 123, 2022)
car2 = Car("Brand 1", "Model 2", 345, 2023)
car3 = Car("Brand 2", "Model 3", 456, 2021)
car4 = Car("Brand 3", "Model 4", 567, 2023)
car5 = Car("Brand 3", "Model 5", 789, 2022)
car6 = Car("Brand 4", "Model 6", 891, 2021)

manufacturer1.add_car(car1)
manufacturer1.add_car(car2)
manufacturer1.add_car(car3)



######################## FOUND THE CAR WITH BRAND ##############################
target_brand = "Brand 1"
target_chassis = 345

car = manufacturer1.get_car_by_brand_and_chassis(target_brand, target_chassis)
if car:
    print("Car Found:")
    print(f"Brand: {car.get_brand()}, Model: {car.get_model()}, Year: {car.get_year()}")
else:
    print("Car Not Found.")


############################### NOT FOUND THE CAR WITH BRAND ###################
target_brand = "Brand 1"
target_chassis = 893

car = manufacturer1.get_car_by_brand_and_chassis(target_brand, target_chassis)
if car:
    print("Car Found:")
    print(f"Brand: {car.get_brand()}, Model: {car.get_model()}, Year: {car.get_year()}")
else:
    print("Car Not Found.")

# Print the details of the cars
# print("Car details:")
# car1.get_details()
# car2.get_details()
# car3.get_details()
# car4.get_details()
# car5.get_details()
# car6.get_details()

