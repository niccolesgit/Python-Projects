# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:36:10 2021

@author: leen8
"""
line = ""
for i in range(9):
    for j in range(9):
        line = line + str(i)+","+str(j)+" "
        if j % 3 ==2:
            line += "  "
            
    if i % 3 ==0 or i % 3 ==1 or i % 3 ==2:
        line += "\n"
        if i % 3 ==2:
            line += "\n"
print(line)

def print_sudoku(board):
    print("-"*25)
    for i, row in enumerate(board):
        print(("|"+" {} {} {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("-"*25)
        else:
            print(" "*9)
print_sudoku(bd)