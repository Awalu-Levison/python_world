#!/usr/bin/python3
#Creating a dictionary
dictionary = {} # Curly braces method
dictionary2 = dict() # With dict()
print(type(dictionary))
print(type(dictionary2))
print(dictionary == dictionary2)

# Populate the dictionary
dictionary["key 1"] = "AWALU LEVISON"
dictionary["key 2"] = "IS"
dictionary["key 3"] = "SOFTWARE ENGINEER"

print("Values in dictionary are: {:s} {:s} {:s} ".format(dictionary["key 1"], dictionary["key 2"], dictionary["key 3"]))
