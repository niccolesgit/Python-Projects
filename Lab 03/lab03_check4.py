# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:08:20 2021

@author: Nicole Lee
"""
def bpop_next(bpop, fpop):
    bpop_next = (10*bpop)/(1+0.1*bpop) -0.05*bpop*fpop
    return int(max(0, bpop_next))
def fpop_next(bpop, fpop):
    fpop_next = 0.4 * fpop + 0.02 * fpop * bpop
    return int(max(0, fpop_next))
pbun = input("Number of bunnies ==> ")
print(pbun)
pfox = input("Number of foxes ==> ")
print(pfox)
pbun = int(pbun)
pfox = int(pfox)

print("Year 1: {} {}".format(pbun, pfox))
y2b = bpop_next(pbun, pfox)
y2f = fpop_next(pbun, pfox)
print("Year 2: {} {}".format(y2b, y2f))
y3b = bpop_next(y2b, y2f)
y3f = fpop_next(y2b, y2f)
print("Year 3: {} {}".format(y3b, y3f))
y4b = bpop_next(y3b, y3f)
y4f = fpop_next(y3b, y3f)
print("Year 4: {} {}".format(y4b, y4f))
y5b = bpop_next(y4b, y4f)
y5f = fpop_next(y4b, y4f)
print("Year 5: {} {}".format(y5b, y5f))

