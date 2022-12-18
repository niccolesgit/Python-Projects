# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:24:42 2021

@author: Nicole lee
"""
co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
A = [int(a) for a in co2_levels]
def is_increasing(L):
    for i in range(len(L)): 
        if (all(i < j for i, j in zip(L, L[1:]))):
            return True
        else:
            return False
print('co2_levels is increasing: {}'.format(is_increasing(A)))
test_L1 = [ 15, 12, 19, 27, 45 ]
print('test_L1 is increasing: {}'.format(is_increasing(test_L1)))
test_L2 = [ 'arc', 'circle', 'diameter', 'radius', 'volume', 'area' ]
print('test_L2 is increasing: {}'.format(is_increasing(test_L2)))
test_L3 = [ 11, 21, 19, 27, 28, 23, 31, 45 ]
print('test_L3 is increasing: {}'.format(is_increasing(test_L3)))

