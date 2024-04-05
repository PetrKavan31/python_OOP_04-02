
# Implement a class Car. Class fields should store the following:
# model, year of release, manufacturer, engine capacity,
# color, price. Implement class methods for data input and output,
# provide access to individual fields through class methods.

class Car:

    def __init__(self, model, year_of_release, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year_of_release
        self.manufacturer = manufacturer
        self.engine = engine_capacity
        self.color = color
        self.price = price

    def

car1 = Car("Civic", 2004, "Honda", 1.6, "grey", 1500)
car2 = Car("Fusion", 2010, "Ford", 1.4, "red", 5000)
