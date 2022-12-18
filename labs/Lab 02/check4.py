# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:16:12 2021

@author: Nicole Lee
"""
nfirst = input("Please enter your first name: ")
nsec = input("Please enter your last name: ")
intro = "Hello, "
lintro = int((len(intro)+7))
firstleng = len(nfirst)
secleng = len(nsec)
firstlengdif = lintro-firstleng-5
seclengdif = lintro-secleng-6

print("*"*lintro)
print("** {}  **".format(intro))
print("** {}".format(nfirst)+" "*firstlengdif+"**")
print("** {}!".format(nsec)+" "*seclengdif+"**")
print("*"*lintro)
          
