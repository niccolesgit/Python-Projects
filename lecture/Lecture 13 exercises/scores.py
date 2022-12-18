# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:31:27 2021

@author: leen8
"""
in_file = input("Enter the scores file: ")
print(in_file)
out_file = input("Enter the output file: ")
print(out_file)

with open(in_file) as inf:
    in_list = [line.strip('\n') for line in inf]
in_list = [ int(x) for x in in_list ]
in_list.sort()
outf = open(out_file, 'w')
c = 0
for i in in_list:
    outf.write("{:2d}: {:3d}\n".format(c, i))
    c+=1

    
