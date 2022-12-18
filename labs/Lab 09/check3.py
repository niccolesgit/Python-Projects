# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:08:34 2021

@author: leen8
"""
from Date import Date
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]
    
f = open('birthdays.txt').read()
fl1 = f.strip().split("\n")
all_birth = []
months = []
for x in fl1:
   fl2 = x.split(" ")
   fl3 = [int(num) for num in fl2]
   months.append(fl3[1])
   d = Date(fl3[0], fl3[1], fl3[2])
   all_birth.append(str(d))
     
minb = all_birth[0]
maxb = all_birth[0]
for x in all_birth:
    if minb < x:
        minb = x
    else:
        minb = minb
for x in all_birth:
    if maxb > x:
        maxb = x
    else:
        maxb = maxb

print("The oldest birthday is: {}".format(maxb))
print("The youngest birthday is: {}".format(minb))
most_m = months[0]
max_count = 0
for x in months:
    if months.count(x) > max_count:
        max_count = months.count(x)
        most_m = x
print("{} has the most birthdays with {}".format(month_names[most_m], max_count))
    
    
    
    
    
    