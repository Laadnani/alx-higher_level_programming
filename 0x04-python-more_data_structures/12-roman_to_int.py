#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        total = 0
        new = 0
        dig = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for a in reversed(roman_string):
            new = dig[a]
            total += new if total < new * 5 else -new
        return total
    else: 
        return 0
