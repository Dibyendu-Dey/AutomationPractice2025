"""
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""
from copyreg import constructor


class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


tata_nexon = Vehicle(80, 10)
print(f"Maximum speed of the car: {tata_nexon.max_speed}")
print(f"Mileage of the car: {tata_nexon.mileage}")

"""
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
"""


class Bus(Vehicle):
    pass


print("\n")
volvo_9400 = Bus(200, 5)
print(f"Max speed of Volvo9400: {volvo_9400.max_speed}")
print(f"Mileage of Volvo9400: {volvo_9400.mileage}")
