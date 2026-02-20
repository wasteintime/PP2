# Method overriding example

class Vehicle:
    def move(self):
        print("Vehicle moves forward")

class Bicycle(Vehicle):
    def move(self):
        print("Bicycle pedals forward")  # child class replaces parent's method

v = Vehicle()
b = Bicycle()

v.move()
b.move()