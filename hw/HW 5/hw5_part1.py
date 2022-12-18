# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:06:58 2021

@author: leen8
"""
import hw5_util

#takes the grid index, converts it into an integer and gets the input if \
    #the user wants to print or not print the grid
gind = input("Enter a grid index less than or equal to 3 (0 to end): ")
print(gind)
gind = int(gind)
yn = input("Should the grid be printed (Y or N): ")
print(yn)

#allows the y or n to be taken in any case
uyn = yn.upper()

#gets the grid from the hw5_util
grid = hw5_util.get_grid(gind)

#creates counter variables to get the row and columns for the grid
rcount = 0
ccount = 0

#if the user puts Y, it prints the grid and spaces it properly based off if its a single or double digit \
    #it also counts how many times the loop runs on the inside and outside
if uyn == "Y":
    print("Grid {}".format(gind))
    line = ""
    for i in range(len(grid)):
        rcount += 1
        for j in range(len(grid[i])):
            ccount +=1
            if grid[i][j] >= 10:
                line = line + "  {}".format(grid[i][j]) 
            elif grid[i][j] < 10:
                line = line + "   {}".format(grid[i][j])
        if (i % 3 ==0 or i % 3 ==1 or i % 3 ==2) and i != len(grid)-1:
            line += "\n"
    print(line)
#if the user inputs N, or any other character, it still counts how man times the loop runs
else:
    line = ""
    for i in range(len(grid)):
        rcount += 1
        for j in range(len(grid[i])):
            ccount +=1
#prints the amount of rows and calculates the amount of columns by dividing the inner loop 
  #counter by the outer loop counter
print("Grid has {} rows and {} columns".format(rcount, (ccount//rcount)))
rnum = rcount 
cnum = (ccount//rcount)
sloc = hw5_util.get_start_locations(gind)

#function that takes the row and column of the neighbor, and the row and column of the grid, calculates
  #and determines if it is a valid neighbor, appending, sorting, and returning the list. 
def get_nbrs(r, c, rnum, cnum):
    
    all_tup = []
    if r+1 > rnum:
        pass
    if r-1 < 0:
        pass
    if r-1 >=0:
        sval = r-1
        stup = (sval, c)
        all_tup.append(stup)
    if r+1 < rnum:
        nval = r+1
        ntup = (nval, c)
        all_tup.append(ntup)
    
    if c+1 > cnum:
        pass
    if c-1 < 0:
        pass
    if c-1 >= 0:
        wcval = c-1
        wtup = (r, wcval)
        all_tup.append(wtup)
    if c+1 < cnum:
        ecval = c+1
        etup = (r, ecval)
        all_tup.append(etup)
    all_tup.sort()
    return all_tup


#gets the list of valid neighbors, converts the list of neighbors into strings and prints the values
for x in sloc:
    nlist = get_nbrs(x[0], x[1], rnum, cnum)
    ftup = ' '.join([str(item)for item in nlist])
    print("Neighbors of {}:".format(x), ftup)


#takes the given paths and determines if it's valid, if only the row or only the column moves, it's valid, 
  #if both move, it's not valid, and prints the invalid path, and breaks the loop
for x in range(len(hw5_util.get_path(gind)) - 1):
    valid = False
    if(hw5_util.get_path(gind)[x][0]==hw5_util.get_path(gind)[x+1][0]+1):
        valid = True
    elif(hw5_util.get_path(gind)[x][0]==hw5_util.get_path(gind)[x+1][0]-1):
        valid = True
    if(hw5_util.get_path(gind)[x][1]==hw5_util.get_path(gind)[x+1][1]+1):
        valid = True
    elif(hw5_util.get_path(gind)[x][1]==hw5_util.get_path(gind)[x+1][1]-1):
        valid = True
    if(((hw5_util.get_path(gind)[x][0]==hw5_util.get_path(gind)[x+1][0]+1) or \
          (hw5_util.get_path(gind)[x][0]==hw5_util.get_path(gind)[x+1][0]-1)) and \
         ((hw5_util.get_path(gind)[x][1]==hw5_util.get_path(gind)[x+1][1]+1) or \
          (hw5_util.get_path(gind)[x][1]==hw5_util.get_path(gind)[x+1][1]-1))): 
        valid = False
        print('Path: invalid step from {} to {}'.format(hw5_util.get_path(gind)[x],hw5_util.get_path(gind)[x+1]))
        break
#however,if the path is valid, it calculates and determines the total amount of downward and upward shifts, 
  #based on if the grid values of the coordinates in the path are greater than or less than each other
if valid == True:
    print('Valid path')
    cup = 0
    cdown = 0
    for i in range(len(hw5_util.get_path(gind))-1):
        val1 = hw5_util.get_grid(gind)[hw5_util.get_path(gind)[i][0]][hw5_util.get_path(gind)[i][1]]
        val2 =  hw5_util.get_grid(gind)[hw5_util.get_path(gind)[i+1][0]][hw5_util.get_path(gind)[i+1][1]]
        val = abs(val2-val1)
        if val1 > val2:
            cdown += val
        if val1 < val2:
            cup += val   
#prints the downward and upward shifts calculated
    print("Downward {}".format(cdown))
    print("Upward {}".format(cup))
        
        


    
                

    
    
    
        
    

    

        
        
        
        
    
    
    


