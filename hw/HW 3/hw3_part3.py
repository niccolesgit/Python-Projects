# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:53:21 2021

@author: Nicole lee
"""
'imports math'
import math

'takes the input of bears and berry area and converts them int float and integer types for calculations'
bears = input("Number of bears => ")
print(bears)
berries = input("Size of berry area => ")
print(berries)
bears = int(bears)
berries =float(berries)
'sets the number of tourists, total tourists, the starting year, counting year, and remaining years after two calculations'
tourists = 10000
tot_tourists = 0
year = 1 
c_year = 0
r_year = 8
'creates lists for all the bears, berries, and tourists witin the data set'
all_bears =[]
all_berries=[]
all_tourists =[]

'function that calculates the number of tourists based off the number of bears'
def calc_tourists(bears):
    if bears < 4 or bears > 15:
        tot_tourists = 0
    elif bears <= 10:
        tot_tourists = tourists * bears
    elif bears > 10: 
        rem_tourists = bears - 10
        ten_tourists = (tourists*bears)-(rem_tourists*tourists)
        twent_tourists = rem_tourists*20000
        tot_tourists = ten_tourists+twent_tourists
    return tot_tourists
'function that calculates the number of bears and berries in the following years and sets berries to 0 if there are 0 berries left'
def find_next(bears, berries, tourists):
    bears_next = berries/(50*(bears+1)) + bears*0.60 -(math.log(1+tourists,10)*0.1) 
    if berries == 0:
        berries_next = 0.0
    else:
        berries_next = (berries*1.5) -(bears+1)*(berries/14) -(math.log(1+tourists,10)*0.05)
    return (int(bears_next), berries_next)

'prints the columns of years, bears, berries, and tourists of year 1, rounding the berries to the tenth place'
print("{0:<10}{1:<10}{2:<10}{3:<10}".format("Year", "Bears", "Berry", "Tourists"))
print("{0:<10}{1:<10}{2:<10}{3:<10}".format(year, bears, round(berries,1), calc_tourists(bears)))

'adds all the data to their respective lists'
all_bears.append(bears)
all_berries.append(berries)
all_tourists.append(calc_tourists(bears))

'creates and keeps values for the 2nd year'
val1 = find_next(bears, berries, calc_tourists(bears))

'adds the second year data to their respective lists and prints the data'
all_bears.append(val1[0])
all_berries.append(val1[1])
all_tourists.append(calc_tourists(val1[0]))
print("{0:<10}{1:<10}{2:<10}{3:<10}".format(year+1,  val1[0], round(val1[1],1), calc_tourists(val1[0])))

'uses a for loop to calculate the following 8 years, rounding the berries to the tenth place, and adding all the data to their lists'
for i in range(r_year):
    val1 = find_next(val1[0], val1[1], calc_tourists(val1[0]))
    print("{0:<10}{1:<10}{2:<10}{3:<10}".format(i+3, val1[0], round(val1[1], 1), calc_tourists(val1[0])))
    all_bears.append(val1[0])
    all_berries.append(val1[1])
    all_tourists.append(calc_tourists(val1[0]))
'gets the minimum of bears, berries, and tourists'
min_bears = min(all_bears)
min_berry = min(all_berries)
min_tourists = min(all_tourists)

'gets the maximum of bears, berries, and tourists'
max_bears = max(all_bears)
max_berry = max(all_berries)
max_tourists = max(all_tourists)

'prints the max and min of all the data'
print("\n{0:<10}{1:<10}{2:<10}{3:<10}".format("Min:", min_bears, round(min_berry,1), min_tourists))
print("{0:<10}{1:<10}{2:<10}{3:<10}".format("Max:", max_bears, round(max_berry,1), max_tourists))



