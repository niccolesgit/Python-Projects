# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 20:40:25 2021

@author: leen8
"""
import hw5_util

#takes the grid index, converts it into an integer and gets the input if \
    #the user wants to print or not print the grid
gind = input("Enter a grid index less than or equal to 3 (0 to end): ")
print(gind)
ms_height = input("Enter the maximum step height: ")
print(ms_height)
gind = int(gind)
ms_height = int(ms_height)
yn = input("Should the path grid be printed (Y or N): ")
print(yn)


#allows the y or n to be taken in any case
uyn = yn.upper()

#gets the grid from the hw5_util
grid = hw5_util.get_grid(gind)

#creates counter variables to get the row and columns for the grid
rcount = 0
ccount = 0
for i in range(len(grid)):
        rcount += 1
        for j in range(len(grid[i])):
            ccount +=1

#prints the amount of rows and calculates the amount of columns by dividing the inner loop 
  #counter by the outer loop counter
print("Grid has {} rows and {} columns".format(rcount, (ccount//rcount)))
#find the maximum value in the grid
maxes = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        max_val = max(grid[i])
    maxes.append(max_val)
amax = max(maxes)

# a fucntion that takes the maximum value and finds its cooresponding coordinate in the grid, returns the coordinate as a tuple
def find_max_coord(amax):
    for i in range(len(grid)):
        if amax in grid[i]:
            x = i
            y = grid[i].index(amax)
    return x, y
max_coord = find_max_coord(amax)
print("global max: {} {}".format(max_coord, amax))

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

rnum = rcount 
cnum = (ccount//rcount)
sloc = hw5_util.get_start_locations(gind)
  
#function that intakes the index, max coordinates, the max step height, and the amount of rows and columns, if the index is witin the start locations and 
#  the range of 2 creates a boolean value to determines the output and iterates through the loop
def grid_path(gind, max_coord, ms_height, rcount, ccount):
    for i in hw5_util.get_start_locations(gind):
        for j in range(2):
            boolean = True
            x = i
            #starts the loop by printing and formatting strings
            if j == 0:
                print("===")
                print("steepest path")
                line = ""
                line += str(i) + " "
                c = 0
                # while the boolean does not equal false, it goes through the grid with the specified coordinates and finds and compares the values to find the path through the neighbors 
                # function, it assigns ans changes the boolean value once it goes through the path 
                while boolean != False:
                    boolean = False
                    z = 0 
                    
                    for a in range(0, len(get_nbrs(x[0], x[1], rcount, ccount))):
                        if(int(hw5_util.get_grid(gind)[get_nbrs(x[0], x[1], rcount, ccount)[a][0]][get_nbrs(x[0], x[1], rcount, ccount)[a][1]])>int(hw5_util.get_grid(gind)[x[0]][x[1]])):
                            if (int(hw5_util.get_grid(gind)[get_nbrs(x[0], x[1], rcount, ccount)[a][0]][get_nbrs(x[0], x[1], rcount, ccount)[a][1]])-int(hw5_util.get_grid(gind)[x[0]][x[1]]))<=ms_height:
                                if z<((int(hw5_util.get_grid(gind)[get_nbrs(x[0], x[1], rcount, ccount)[a][0]][get_nbrs(x[0], x[1], rcount, ccount)[a][1]]))-int(hw5_util.get_grid(gind)[x[0]][x[1]])):
                                    z = int(hw5_util.get_grid(gind)[get_nbrs(x[0], x[1], rcount, ccount)[a][0]][get_nbrs(x[0], x[1], rcount, ccount)[a][1]])-int(hw5_util.get_grid(gind)[x[0]][x[1]])
                                    k = get_nbrs(x[0], x[1], rcount, ccount)[a][0],get_nbrs(x[0], x[1], rcount, ccount)[a][1]
                                    boolean = True
                    #if the boolean is true, it counts into a counter variable and if the counter has no remainder after modular division, and if the boolean 
                    # is true, it adds a bath and spacing to the line with the path
                    if boolean == True:
                        c+=1
                        if c%5==0 and boolean == True:
                            line += "\n" + str(k)+" "
                        elif c%5!=0 and boolean == True:
                            line += str(k)+" "
                    # assigns the values found in x to x for it to be compared 
                    x = k
                print(line)
                #determines if the coordinate equals the max coordinate and prints that it is a global maximum, if not, its prints that it's not a maximum
                if(x[0] == max_coord[0] and x[1] == max_coord[1]):
                    print("global maximum")
                else:
                    print("no maximum")
            # finds and starts the loop for the gradual path
            elif(j==1):
                print("...")
                print("most gradual path")
                line = ""
                line += str(x) + " "
                c = 0
                # similarly goes the loop as the steepest path, but goes through all the coordinates to find the gradual path instead, through comparing the values
                # of the coordinates from the get neighbors funciton
                while(boolean != False):
                    boolean = False
                    g = 100
                    for a in range(0, len(get_nbrs(x[0], x[1], rcount, ccount))):
                        if(hw5_util.get_grid(gind)[get_nbrs(x[0], x[1], rcount, ccount)[a][0]][get_nbrs(x[0], x[1], rcount, ccount)[a][1]]>hw5_util.get_grid(gind)[x[0]][x[1]]):
                            if (int(hw5_util.get_grid(gind)[get_nbrs(x[0], x[1], rcount, ccount)[a][0]][get_nbrs(x[0], x[1], rcount, ccount)[a][1]])-int(hw5_util.get_grid(gind)[x[0]][x[1]]))<=ms_height:
                                if g>((int(hw5_util.get_grid(gind)[get_nbrs(x[0], x[1], rcount, ccount)[a][0]][get_nbrs(x[0], x[1], rcount, ccount)[a][1]]))-int(hw5_util.get_grid(gind)[x[0]][x[1]])):
                                    g = int(hw5_util.get_grid(gind)[get_nbrs(x[0], x[1], rcount, ccount)[a][0]][get_nbrs(x[0], x[1], rcount, ccount)[a][1]])-int(hw5_util.get_grid(gind)[x[0]][x[1]])
                                    l = get_nbrs(x[0], x[1], rcount, ccount)[a][0],get_nbrs(x[0], x[1], rcount, ccount)[a][1]
                                   
                                    boolean = True
                    #if the boolean is true, it counts into a counter variable and if the counter has no remainder after modular division, and if the boolean 
                    # is true, it adds a bath and spacing to the line with the path
                    if boolean == True:
                       c+=1
                       if c%5==0:
                           line += "\n" + str(l) + " "
                       elif c%5!=0:
                           line += str(l)+ " "
                    x=l
                print(line)
                #determines if the coordinate equals the max coordinate and prints that it is a global maximum, if not, its prints that it's not a maximum
                if(x[0] == max_coord[0] and x[1] == max_coord[1]):
                    print("global maximum")
                else:
                    print("no maximum")
#takes the index from the user and prints the proper steep and gradual path based on the index, max step height, and the total number of rows and columns. 
if gind == 1:
    grid_path(gind, max_coord, ms_height,rcount, ccount//rcount)
elif gind == 2:
     grid_path(gind, max_coord, ms_height,rcount, ccount//rcount)
elif gind == 3:
    grid_path(gind, max_coord, ms_height,rcount, ccount//rcount)   
                                
                    
    



