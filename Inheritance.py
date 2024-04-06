
# Create a Ship class containing information about a ship.
# Use inheritance to implement a Frigate class (contains
# info about a frigate), a Destroyer class (contains info about
# a destroyer), a Cruiser class (contains info about a cruiser).
# Each class must have the required methods.

class Ship:
    def __init__(self, name, length, speed):
        self.name = name
        self.length = length
        self.speed = speed

    def show_msg(self):
        return (f"I am warship {self.name}, my length is {self.length} m and my speed is {self.speed} knots")


class Frigate(Ship):
    def __init__(self, name, length, speed, spec):
        super().__init__(name, length, speed)
        self.spec = spec

    def show_msg(self):
        print(f"{super().show_msg()} and my special power is: {self.spec}!")


class Destroyer(Ship):
    def __init__(self, name, length, speed, spec):
        super().__init__(name, length, speed)
        self.spec = spec

    def show_msg(self):
        print(f"{super().show_msg()} and my special power is: {self.spec}!")


class Cruiser(Ship):
    def __init__(self, name, length, speed, spec):
        super().__init__(name, length, speed)
        self.spec = spec

    def show_msg(self):
        print(f"{super().show_msg()} and my special power is: {self.spec}!")


frigate1 = Frigate("USS Leahy", 162, 32, "radars")
destroyer1 = Destroyer("USS Winston S. Churchill", 155, 30, "torpedoes")
cruiser1 = Cruiser("USS Arkansas", 178, 30, "missiles")

frigate1.show_msg()
destroyer1.show_msg()
cruiser1.show_msg()