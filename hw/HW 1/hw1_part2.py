# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:58:25 2021

@author: Nicole lee
"""
'prompts user for their inputs'
minute = input("Minutes ==> ")
print(minute)
sec = input("Seconds ==> ")
print(sec)
mile = input("Miles ==> ")
print(mile)
tmile = input("Target Miles ==> ")
print(tmile)

'changes inputs into float types'
minute = float(minute)
sec = float(sec)
mile = float(mile)
tmile = float(tmile)

'calculates pace'
smins = minute*60+sec
cpace = smins/mile
rpace = cpace/60 

'calculates and formats speed'
hour = smins/60/60
speed = mile/hour
aspeed = round(speed, 2)
fspeed = "{:.2f}".format(aspeed)

'separates and calculates the minutes and seconds of speed'
mpace = int(rpace)
space = int((rpace - mpace)*60)

'calculates and formats predicted time for target distance, and separates minutes and seconds for predicted time'
rpmtime = rpace*tmile
pmtime = int(rpace*tmile)
pstime = int((rpmtime-pmtime)*60)
fmile =  "{:.2f}".format(tmile)

'prints all calculations'
print("\nPace is {} minutes and {} seconds per mile.".format(mpace, space))
print("Speed is {} miles per hour.".format(fspeed))
print("Time to run the target distance of {} miles is {} minutes and {} seconds.".format(fmile, pmtime, pstime))

