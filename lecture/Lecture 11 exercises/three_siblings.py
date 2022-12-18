# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:18:21 2021

@author: Nicole Lee
"""
hd = input("Enter Dale's height: ")
print(hd)
he = input("Enter Erin's height: ")
print(he)
hs = input("Enter Sam's height: ")
print(hs)

hd = int(hd)
he = int(he)
hs = int(hs)
first = ""
second = ""
third = ""
if hd > he and hd > hs:
    first = "Dale"
    if he > hs:
        second = "Erin"
        third = "Sam"
    if hs > he:
        second = "Sam"
        third = "Erin"
elif he > hd and he > hs:
    first = "Erin"
    if hd > hs:
        second = "Dale"
        third = "Sam"
    if hs > hd:
        second = "Sam"
        third = "Dale"
elif hs > hd and hs > he:
    first = "Sam"
    if hd > he:
        second = "Dale"
        third = "Erin"
    if he > hd:
        second = "Erin"
        third = "Dale"
print(first + "\n" + second + "\n" + third)




