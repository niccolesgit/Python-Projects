# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:37:11 2021

@author: User
"""
record = []
def move_pokemon (tup, direct, step):
    udirect = direct.upper()
    loc = list(tup)
    if udirect == "N":
        loc[0] -= step
    elif udirect == "E":
        loc[1] += step
    elif udirect == "S":
        loc[0] += step
    elif udirect == "W":
        loc[1] -= step
    if loc[0] < 0:
        loc[0] = 0
    if loc[1] < 0:
        loc[1] = 0
    return tuple(loc)

start = (75, 75)
turns = input("How many turns? => ")
print(turns)
name = input("What is the name of your pikachu? => ")
print(name)
oturns = input("How often do we see a Pokemon (turns)? => ")
print(oturns)
turns = int(turns)
oturns = int(oturns)

turns_c = 0
oturns_c = 0
cturns_c = 0
record = []
steps = 5
nopp = "S"
sopp = "N"
wopp = "E"
eopp = "W"
wstep = 1
lstep = 10 
print("Starting simulation, turn {} {} at ({}, {})".format(
    turns_c, name, start[0], start[1]))
while oturns_c < oturns:
    direct = input("What direction does "+name+" walk? => ")
    print(direct)
    udirect = direct.upper()
    start = newplace
    if  udirect == "N":
        for x in range(turns_c+1):
            start = move_pokemon(start, udirect, steps)
    elif udirect == "S":
        for x in range(turns_c+1):
            start = move_pokemon(start, udirect, steps)
    elif udirect == "E":
        for x in range(turns_c+1):
            start = move_pokemon(start, udirect, steps)
    elif udirect == "W":
        for x in range(turns_c+1):
            start = move_pokemon(start, udirect, steps)
    if start[0] < 0:
        start[0] = 0
    if start[1] < 0:
        start[1] = 0
    oturns_c += 1
    print("Turn {}, {} at {}".format(oturns_c, name, start))
    newplace = start
    ptype = input("What type of pokemon do you meet (W)ater, (G)round? => ")
    print(ptype)
    uptype = ptype.upper()
    if uptype == "G":
        if udirect == "N":
            newplace = move_pokemon(newplace, nopp, lstep)
        if udirect == "S":
            newplace = move_pokemon(newplace, sopp, lstep)
        if udirect == "E":
            newplace = move_pokemon(newplace, eopp, lstep)
        if udirect == "W":
            newplace = move_pokemon(newplace, wopp, lstep)
        print("{} runs away to {}".format(name, newplace))
        record.append("Win")
    elif uptype == "W":
        if udirect == "N":
            newplace = move_pokemon(newplace, udirect, wstep)
        if udirect == "S":
            newplace = move_pokemon(newplace, udirect, wstep)
        if udirect == "E":
            newplace = move_pokemon(newplace, udirect, wstep)
        if udirect == "W":
            newplace = move_pokemon(newplace, udirect, wstep)
        print("{} runs away to {}".format(name, newplace))
        record.append("Lose")
    else:
        record.append("No Pokemon")
        
        
    
    

