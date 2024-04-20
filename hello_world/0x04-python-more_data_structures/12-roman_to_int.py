#!/usr/bin/python3

def roman_to_int(roman_string):
    romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    temp_number = 0
    if type(roman_string) is not str or roman_string is None:
        return (0)
    for j, char in enumerate(roman_string):
        temp_value = romans[char]
        try:
            if temp_value < romans[roman_string[j + 1]]:
                temp_value = temp_value * -1
        except IndexError:
            pass
        temp_number = temp_number + temp_value
    return temp_number
