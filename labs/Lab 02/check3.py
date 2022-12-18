# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:20:47 2021

@author: Nicole Lee
"""
word = input("Enter a word: ")
wordleng = int((len(word)+6))

print("*" * wordleng)
print("** {} **".format(word))
print("*" * wordleng)
