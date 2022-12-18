# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:50:47 2021

@author: leen8
"""
def find_min(l):
    min_list = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            min_list.append(min(l[i]))
    return min(min_list)
            

if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )