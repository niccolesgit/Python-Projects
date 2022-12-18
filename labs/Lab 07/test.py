# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:10:35 2021

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

def get_line(fname,parno,lineno):
    f = open(fname, encoding='utf8').read()
    plist = f.split("\n\n")
    para = plist[parno]
    llist = para.split("\n")
    line = llist[lineno]
    return line


fname = input("Please enter the file number ==> ")
parno = input("Please enter the paragraph number ==> ")
parno = int(parno)
lineno = input("Please enter the line number ==> ")
lineno = int(lineno)

fname = fname + ".txt"
parno -= 1
lineno -=1
line = get_line(fname, parno, lineno)
while line != "END/0/0/0":
    if line != "/n/n":
        if parse_line(line) != None:
        
        
    
