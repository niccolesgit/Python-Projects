# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:23:39 2021

@author: leen8
"""
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
L2 = [1]
L3 = [17, 16.2, -3, 2.5, 9.0, 19, 1, 1.5]
def closest1(L1):
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
        return min1, min2

if __name__ == "__main__":
    print(closest1(L1))
