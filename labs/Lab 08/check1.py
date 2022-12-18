# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:30:37 2021

@author: leen8
"""
def get_words(file):
    f = open(file).read()
    ofile = f.strip("\n").split("|")
    del ofile[0]
    nf = ''.join(ofile).lower()
    punct = '''()"\,.'''
    for i in nf:
        if i in punct:
            nf = nf.replace(i, "")
    nofile = nf.split(" ")
    nlist = []
    for x in nofile:
        if x.isalpha() == False:
            nofile.remove(x)
    for y in nofile:
        if len(y) >= 4:
            nlist.append(y)
    slist = set(nlist)
    return slist
file = input("Enter a file: ")
file += ".txt"
print("File {}.txt {} words".format(file, len(get_words(file))))
print(get_words(file))