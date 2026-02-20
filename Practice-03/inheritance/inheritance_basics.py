# Parent and child class example

class Vehicle:  # parent class
    def start_engine(self):
        print("Engine starts")

class Car(Vehicle):  # child class inherits from Vehicle
    pass  # inherits all methods and properties from Vehicle

my_car = Car()
my_car.start_engine()

