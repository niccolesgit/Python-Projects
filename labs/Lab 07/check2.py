# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 01:19:11 2021

@author: leen8
"""
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
print(get_line(fname, parno, lineno))
