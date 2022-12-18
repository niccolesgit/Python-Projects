# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:32:12 2021

@author: leen8
"""
import random
import time
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]

def closest1(L1):
    '''
    >>> closest1(L1)
    (5.4, 4.3)
    '''
    L4 = L1.copy()
    if len(L1) < 2:
        return (None, None)
    else:
        alltup = []
        for i in range(len(L1)-1):
            x = L1[i]
            for j in range(len(L4)-1):
                y = L4[j+1]
                tup = (x,y)
                alltup.append(tup)
        diffl = []
        mindiff = alltup[0][1] - alltup[0][0]
        for x in alltup:
            diff = abs(x[1] - x[0])
            diffl.append(diff)
        odiffl = diffl.copy()
        for y in diffl:
            if y == 0.0:
                diffl.remove(y)
        mindiff = min(diffl)
        indiff = odiffl.index(mindiff)
        mintup = alltup[indiff]
        return mintup

def closest2(L1):
    '''
    >>> closest1(L1)
    (5.4, 4.3)
    '''
    if len(L1) < 2:
        return (None, None)
    else:
        L4 = L1.copy()
        L4.sort()
        diff = []
        for x in range(len(L4)-1):
            diff1 = L4[x+1]-L4[x]
            diff.append(diff1)
        mindiff = min(diff)      
        minind = diff.index(mindiff)
        min1 = L4[minind]
        min2 = L4[minind+1]
        mintup = (min1, min2)
        return mintup


ulist = []
if __name__ == "__main__":
    n = int(input("Enter the number of values to test ==> "))
    for i in range(0, n):
        ulist.append(random.uniform(0.0, 1000.0))
    t = time.time()
    closest1(ulist)
    t3 = time.time()
    print(t3-t)
    t = time.time()
    closest2(ulist)
    t4 = time.time()
    print(t4-t)
  #the first method takes longer because when there is a nested for loop, it takes the time and it increases exponentionally
  # meanwhile the second method takes shorter time because there is only one for loop and it increases linearlly. 