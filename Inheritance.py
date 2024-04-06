
# Create a Ship class containing information about a ship.
# Use inheritance to implement a Frigate class (contains
# info about a frigate), a Destroyer class (contains info about
# a destroyer), a Cruiser class (contains info about a cruiser).
# Each class must have the required methods.

class Ship:
    def __init__(self, name, length, speed ):
        self.name = name
        self.length = length
        self.speed = speed

    def show_msg(self):
        print(f"I am warship {self.name}, my length is {self.length} m and my speed is {self.speed} knots.")

class Frigate(Ship):
    def __init__(self, name, length, speed, spec):
        super.__init__(name, length, speed)
        self.spec = spec


frigate1 = Frigate("USS Leahy", 162, 32, "radars")


class Destroyer(Ship):
    def __init__(self, name, length, speed, spec):
        super.__init__(name, length, speed)
        self.spec = spec


destroyer1 = Destroyer("USS Winston S. Churchill", 155, 30, "torpedoes")


class Cruiser(Ship):
    def __init__(self, name, length, speed, spec):
        super.__init__(name, length, speed)
        self.spec = spec


cruiser1 = Cruiser("USS Arkansas", 178, 30, "missiles")
