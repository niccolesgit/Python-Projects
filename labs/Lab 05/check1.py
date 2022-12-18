# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:34:15 2021

@author: Nicole Lee
"""
import lab05_util 
restaurants = lab05_util.read_yelp('yelp.txt')
def print_info(resturant_list):
    name = resturant_list[0]
    street = resturant_list[3]
    spl_street = street.split("+")
    if len(spl_street) == 3:
        tstreet = spl_street[0] + "\n\t" + spl_street[1] + "\n\t" + spl_street[2]
    else:
        tstreet = spl_street[0] + "\n\t" + spl_street[1]
    pl_type = resturant_list[5]
    lavg = resturant_list[-1]
    avg = sum(lavg) / len(lavg)
    print(name + " ({})".format(pl_type)+ "\n\t" + tstreet + "\n" + "Average score: {:.2f}".format(avg) + "\n")
print_info(restaurants[0])
print_info(restaurants[4])
print_info(restaurants[42])
