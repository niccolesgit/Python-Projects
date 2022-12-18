# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:48:01 2021

@author: leen8
"""

def parse_line(line):
    line1 = line.split("/")
    digits = []
    for x in line1:
        if x.isdigit():
            digits.append(x)
    if len(digits) > 3 or len(digits) < 3:
        return None
    else:
        line1.pop()
        line1.pop()
        line1.pop()
        line1 = tuple(line1)
        line2 = "/".join(line1)
        digits.append(line2)
        
    return tuple(digits)
print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line("        Here is some spaces 12/32/4"))
print(parse_line("       Again some spaces\n/12/12/12"))
print(parse_line("END/0/0/0"))