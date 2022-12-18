# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:50:18 2021

@author: Nicole Lee
"""
'function that moves the pokemon by column and row'
def move_pokemon (row, column, direct, step):
    udirect = direct.upper()
    if udirect == "N":
        if (row-step>=0):
            row -= step
        else:
            row = 0 
    if udirect == "S":
        if (row+step<=150):
            row += step
        else:
            row = 150
    if udirect == "E":
        if (column+step<=150):
            column += step
        else:
            column = 150 
    if udirect == "W":
        if (column-step>=0):
            column -= step
        else:
            column = 0
    loc = (row, column)
    return loc
'sets row and column to the start position (75, 75)'
row = 75
column = 75

'takes and converts inputs from the user'
turns = input("How many turns? => ")
print(turns)
name = input("What is the name of your pikachu? => ")
print(name)
oturns = input("How often do we see a Pokemon (turns)? => ")
print(oturns)
turns = int(turns)
oturns = int(oturns)

'sets the counter variables by amount of often turns, creates the record list, winning, losing, and normal steps'
o_turn = 0 
i_turn = 0 
record = []
step = 5
wstep = 1
lstep = 10 
'starts the simulation, breaks if conditons are not met' 
print("\nStarting simulation, turn 0 {} at ({}, {})".format(name, row, column))
while(o_turn < turns):
    i_turn = 0
    while i_turn < oturns:
        if (i_turn >= turns):
            break
        'determines the direction from the user and converts it to be taken in any case then incriments the loop and calls the function multiple times'
        direct = input("What direction does {} walk? => ".format(name))
        print(direct)
        udirect = direct.upper()
        row = move_pokemon(row, column, udirect, step)[0]
        column = move_pokemon(row, column, udirect, step)[1]
        i_turn += 1
        o_turn += 1
        "breaks when the often or counter turns are more than the normal turns "
        if (o_turn>turns):
            break
    if(oturns > turns):
        break
    if(o_turn>turns):
       break
    'prints the new location and starts the battle for the pokemon'
    print("Turn {}, {} at ({}, {})".format(o_turn, name, row, column))
    p_type = input("What type of pokemon do you meet (W)ater, (G)round? => ")
    print(p_type)
    up_type = p_type.upper()
    'determines and calculates the proper directions of a win or loss against a ground and water type '
    if up_type == "G":
        record.append("Lose")
        if udirect == "N":
            row += lstep
        if udirect == "S":
            row -= lstep
        if udirect == "E":
            column -= lstep
        if udirect == "W":
            column += lstep
        print("{} runs away to ({}, {})".format(name, row, column))
    elif up_type == "W":
        record.append("Win")
        if udirect == "N" or udirect == "S":
            row = move_pokemon(row, column, direct, wstep)[0]
        if udirect == "E" or udirect == "W":
            column = move_pokemon(row, column, direct, wstep)[1]
        print("{} wins and moves to ({}, {})".format(name, row, column))
    else:
        record.append("No Pokemon")
'prints the final location and record'
print("{} ends up at ({}, {}), Record: {}".format(name, row, column, record))