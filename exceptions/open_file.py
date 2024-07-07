#!/usr/bin/python3
"""
A program that ope a file
raise an exception error when trying to open file
that doesnt exist
"""
try:
    myFile = open("text1.txt", encoding="utf-8")

except FileNotFoundError as e:
    print("There is no such file")
    print(e.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("End of using the file")
