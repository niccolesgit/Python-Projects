# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:23:39 2021

@author: leen8
"""
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
L2 = [1]
L3 = [17, 16.2, -3, 2.5, 9.0, 19, 1, 1.5]

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

if __name__ == "__main__":
    pass
    