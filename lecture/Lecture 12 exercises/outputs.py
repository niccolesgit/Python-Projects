# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:59:40 2021

@author: leen8
"""
# Version 1
total = 0
for i in range(10):
    for j in range(10):
        total += 1
print(total)
# Version 2
total = 0
for i in range(10):
    for j in range(i+1,10):
        total += 1
print(total)
# Version 3
total = 0
for i in range(10):
    total += 1
for j in range(10):
    total += 1
print(total)
