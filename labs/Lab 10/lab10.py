# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:23:39 2021

@author: leen8
"""
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
L2 = [1]
L3 = [17, 16.2, -3, 2.5, 9.0, 19, 1, 1.5]
def addone(x):
    
    return x+1
def closest1(L1):
    if len(L1) < 2:
        return (None, None)
    else:
        L1.sort()
        diff = []
        for x in range(len(L1)-1):
            diff1 = L1[x+1]-L1[x]
            diff.append(diff1)
        mindiff = min(diff)      
        minind = diff.index(mindiff)
        min1 = L1[minind]
        min2 = L1[minind +1]
        mintup = (min1, min2)
        return mintup

if __name__ == "__main__":
    pass
print(closest1(L1))
print(closest1(L2))
print(closest1(L3))