# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:15:21 2021

@author: Nicole Lee
"""
import lab05_util 
restaurants = lab05_util.read_yelp('yelp.txt')
def print_info(resturant_list):
    name = resturant_list[0]
    street = resturant_list[3]
    spl_street = street.split("+")
    street1 = spl_street[0]
    street2 = spl_street[1]
    pl_type = resturant_list[5]
    lavg = resturant_list[-1]
    lmax = max(lavg)
    lmin = min(lavg)
    if len(lavg) < 3:
        avg = sum(lavg) / len(lavg) 
    else:
        avg = (sum(lavg)-lmax-lmin) / len(lavg)
    if avg <= 2:
        rate = "bad"
    elif avg > 2 and avg <=3:
        rate = "average"
    elif avg > 3 and avg <=4:
        rate = "above average"
    elif avg > 4 and avg <=5:
        rate = "very good"
    print(name + " ({})".format(pl_type)+ "\n\t" + street1 + "\n\t" + street2 + "\n" + "Average score: {:.2f}".format(avg) + "\n")
    print("This restaurant is rated {}, based on {} reviews.".format(rate, len(lavg)))
while True:
    rest_num = input("Please enter a resturant id: ")
    rest_num = int(rest_num)
    rest_ind = rest_num -1
    if rest_num <= 0:
       print("Error, invalid ID")
       break
    elif rest_num > 0:
       print_info(restaurants[rest_ind])

