# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:59:58 2021

@author: leen8
"""
file = input("Data file name: ").strip()
print(file)
prefix = input("Prefix: ")
print(prefix)


lnames = []
for line in open(file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip().split(",")
    name[0] = name[0].strip()
    lnames.append(name[0])
set_last = len(set(lnames))
slnames = []
for x in range(len(lnames)-1):
    if lnames[x].startswith(prefix) == True:
        slnames.append(lnames[x])
set_lastn = len(set(slnames))
print("{} last names".format(set_last))
print("{} start with {}".format(set_lastn, prefix))

