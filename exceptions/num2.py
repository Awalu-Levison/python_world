#!/usr/bin/python3
"""Exceptions in python"""

num1, num2, = input("Enter two values to divide : ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You cant divide by zero value")

else:
    print("No exception raised so far")

finally:
    print(" I execute it no matter")
