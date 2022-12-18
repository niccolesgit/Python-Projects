# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:56:40 2021

@author: leen8
"""
def parse_line(line):
    line1 = line.split("/")
    digits = []
    for x in line1:
        if x.isdigit():
            digits.append(x)
    if len(digits) > 3 or len(digits) < 3:
        print(line1)
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
    plist = f.strip().split("\n\n")
    para = plist[parno].strip()
    llist = para.strip().split("\n")
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

output = []
count = 0
while count == 0:
    lines = parse_line(get_line(fname, parno, lineno))
    wfile = open("program.py", "w") 
    print(lines)
    output.append(lines[-1])
    fname = str(lines[0])
    fname += ".txt"
    parno = int(lines[1])
    lineno = int(lines[2])
    parno -= 1
    lineno -=1
    if(lines[-1] == "END"):
        for x in output:
            del output[-1]
            wfile.write(x+"\n")
        wfile.close()
        count+=1
