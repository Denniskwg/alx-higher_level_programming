#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    if roman_string and isinstance(roman_string, str):
        if len(roman_string) == 2 and subtractive(roman_string, numerals):
            num = numerals.get(roman_string[1]) - numerals.get(roman_string[0])
        elif len(roman_string) > 2 and subtractive(roman_string, numerals):
            num = numerals.get(roman_string[-1]) - numerals.get(roman_string[-2])
            for i in range(len(roman_string) - 2):
                if numerals.get(roman_string[i]):
                    num += numerals.get(roman_string[i])
                else:
                    continue
        else:
            for i in roman_string:
                if numerals.get(i):
                    num += numerals.get(i)
                else:
                    continue
    else:
        return 0
    return num

def subtractive(string, rom):
    if rom.get(string[0]) < rom.get(string[1]):
        return True
    elif rom.get(string[-2]) < rom.get(string[-1]):
        return True
    else:
        return False
