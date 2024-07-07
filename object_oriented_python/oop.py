#!/usr/bin/python3

""" Basics of objects and classes
in python
"""
class Car:
    def __init__(self, color, weight, ev):
        print("The init function is called")
        print(color, weight, ev)

        self.color = color
        self.weight = weight
        self.isEv = ev

car1 = Car("Black", 12000, True)
car2 = Car("white", 15000, False)

print(car1)
print(car2)
