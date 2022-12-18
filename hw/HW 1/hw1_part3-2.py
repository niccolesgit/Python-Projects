# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:58:54 2021

@author: Nicole lee
"""
'prompt and gains inputs from thNo e user'

'function that creates the box from inputs'
def prin_box(wei, hei, cha):
    mid = f'{wei}x{hei}' 
    topcw = cha * wei
    hspace = ' ' * (wei - 2)
    l_side = len(hspace) - len(mid) 
    r_side = l_side // 2 
    l_side -= r_side 
    top_side = hei - 2 - 1 
    bot_side = top_side // 2 
    top_side -= bot_side 
    hrow = cha + hspace + cha 
    r_cent = [cha + ' ' * l_side + mid + ' ' * r_side + cha] 
    return '\n'.join([topcw] + [hrow] * top_side + r_cent + [hrow] * bot_side + [topcw])

'gets and prints inputs from user'
char = input('Enter frame character ==> ')
print(char)
height = input('Height of box ==> ')
print(height)
width = input('Width of box ==> ')
print(width)

'converts inputs into integers'
height = int(height)
width = int(width)
'prints the final result'
final = prin_box(width, height, char)
print("\nBox:")
print(final)

'prints the box byt printing the characters row by row'
print("\nBox:")
print(char*width)
print(char + " "*(width-2)+ char)
spaces = int((width - height)/2)
print(char + (" "* spaces) + "{}x{}".format(width,height) + (" "*spaces) + char)
print(char + " "*(width-2)+ char)
print(char*width)


