#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    if roman_string and isinstance(roman_string, str):
        if len(roman_string) == 2 and subtractive(roman_string, numerals):
            num = numerals.get(roman_string[1]) - numerals.get(roman_string[0])
        elif len(roman_string) > 2 and subtractive(roman_string, numerals):
            num = calculate_integer(roman_string, numerals)
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

def calculate_integer(string, rom):
    num = 0
    index_length = len(string) - 1
    j = 0
    i = 0
    while i < len(string):
        if rom.get(string[i]):
            j = i + 1
            if i != index_length:
                if rom.get(string[i]) < rom.get(string[j]):
                    num += (rom.get(string[j]) - rom.get(string[i]))
                    if index_length % 2 == 0:
                        i = i + 1
                else:
                    num += rom.get(string[i])
        else:
            continue
        i += 1
    return num
