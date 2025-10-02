class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def drive(self):
        print(f"The {self.brand} is driving")

car_1 = Car("G_wagon", 2020)
car_2 = Car("Ferrari", 2010)
car_1.drive()
car_2.drive()
print(car_2.year)