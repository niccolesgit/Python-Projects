# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:29:12 2021

@author: leen8
"""
from hw5_util import get_start_locations
from hw5_util import get_grid
from hw5_util import get_path
from hw5_util import num_grids

grid =  [[15, 16, 18, 19, 12, 11], 
         [13, 19, 23, 21, 16, 12], 
         [12, 15, 17, 19, 20, 10], 
         [10, 14, 16, 13, 9, 6]]
sloc = get_start_locations(1)
print(sloc)
#(3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2),
#steep path = 10, 14, 16, 17, 19, 21, 23 
# (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2)
#gradual path = 10, 12, 13, 15, 16, 18, 19, 21, 23 


maxes = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        max_val = max(grid[i])
    maxes.append(max_val)
amax = max(maxes)

def find_max_coord(amax):
    for i in range(len(grid)):
        if amax in grid[i]:
            x = i
            y = grid[i].index(amax)
    return x, y
print("global max: {} {}".format(find_max_coord(amax), amax))
for x in range(len(grid)):
    for i in range(len(get_start_locations(1))-1):
        val1 = get_grid(1)[get_start_locations(1)[i][0]][get_start_locations(1)[i][1]]
        

       
            
            
        
