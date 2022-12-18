# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:32:48 2021

@author: leen8
"""
import lab06_util
bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]


def bd_format(bd):
    line = "-"*25 + "\n" + "| "
    for i in range(9):
        for j in range(9):
            line = line + bd[i][j]+" "
            if j % 3 ==2:
                line += "| "
        if i % 3 ==0 or i % 3 ==1 or i % 3 ==2:
            line += "\n" 
            if i % 3 ==2:
                line = line + "-"*25+"\n" + "| "
            else: 
                line += "| "
    return line
def ok_to_add(r, c, val, bd):
    if val in bd[r]:
        return False
    for y in range(9):
        if val == bd[y][c]:
            return False
    brow = r // 3 
    bcol= c // 3
    for i in range(0, 3):
        for j in range(0,3):
            if val == bd[i+brow*3][j+bcol*3]:
                return False
    return True
file = input("Enter a file: ")
f = lab06_util.read_sudoku(file)

def verify_board(r, c, val, f):
    for i in range(9):
        for j in range(9):
            if f[i][j] != "." and ok_to_add(r, c, val, f) == False:
                return False
            else:
                return True
        

while True:
    r = input("Please enter a row: ")
    r = int(r)
    c = input("Please enter a column: ")
    c = int(c)
    val = input("Please enter a value: ")
    if verify_board(r, c, val, f) == True: 
        if ok_to_add(r, c, val, bd) == True:
           x = f.replace(f[r][c], val)
           print(bd_format(x))
    else:
        break
print(bd_format(x))
        
       
