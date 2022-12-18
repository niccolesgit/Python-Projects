# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:37:01 2021

@author: leen8
"""

def bubble_sort(data):
    for _ in range(len(data)):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    for x in data:
        if x 

a_list = [2, 1, 5, 4, 3]

sorted_list = bubble_sort(a_list)

print(sorted_list)
