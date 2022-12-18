"""
This program experiments with the use of functions
and also learning error checking.


"""
import math
## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
def line_length(x1,y1,x2,y2):
    length = (x1-x2)**2 + (y1-y2)**2
    length = math.sqrt(length)
    return length


initial_x = 10
initial_y = 10
next_x = input("The next x value ==> ")
next_y = input("The next y value ==> ")
next_x = int(next_x)
next_y = int(next_y)


print("The point has moved from ({:d},{:d}) to ({:d},{:d})".format(initial_x, initial_y, next_x, next_y))

print("Total length traveled is {:.2f}".format(line_length(initial_x, initial_y, next_x, next_y)))

