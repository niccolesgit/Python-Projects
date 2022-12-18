# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:04:00 2021

@author: Nicole Lee
"""
def earlier_semester(tup1, tup2):
    if tup1[0] == "Spring" and tup2[0] == "Fall":
        if tup1[1] > tup2[1]:
            return False
        elif tup1[1] == tup2[1]:
            return True
        else:
           return True 
    elif tup1[0] == "Fall" and tup2[0] == "Spring":
         if tup1[1] > tup2[1]:
            return False
         elif tup1[1] == tup2[1]:
            return False
         else:
            return True 
    elif tup1[0] == tup2[0]:
        if tup1[1] > tup2[1]:
            return False
        elif tup1[1] < tup2[1]:
            return True
        else:
            return False
w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))