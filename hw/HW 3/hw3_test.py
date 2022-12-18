# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:27:34 2021

@author: User
"""
from untitled2 import move_pokemon
row = 15
column = 10

print(move_pokemon((row, column) , 'n' , 20)) # should print (0, 10) 
print(move_pokemon((row, column) , 'e' , 20)) # should print (15, 30) 
print(move_pokemon((row, column) , 's' , 20)) # should print (35, 10) 
print(move_pokemon((row, column) , 'w' , 20)) # should print (15, 0)

