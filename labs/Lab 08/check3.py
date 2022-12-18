# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:29:23 2021

@author: leen8
"""
def get_words(line):
    ofile = line.strip("\n").split("|")
    punct = '''()"\,.'''
    ofile = ''.join(ofile).lower()
    i = ""
    if i in punct:
        nf = ofile.replace(i, "")
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
file1 = input("Please enter a club file: ")
file2 = "allclubs.txt"
f2 = open(file2)
clubs = dict()
for x in f2:
    data = x.split("|")
    clubs[data[0].lower()] = data[1]
words1 = get_words(clubs[file1])
comwl = []
keyl = []
topfive = []
for key in clubs.keys():
    words2 = get_words(clubs[key])
    both = words1.intersection(words2)
    lboth = len(both)
    comwl.append(lboth)
    keyl.append(key)
ocomwl = comwl.copy()
m1 = max(comwl)
comwl.remove(m1)
m2 = max(comwl)
comwl.remove(m2)
m3 = max(comwl)
comwl.remove(m3)
m4 = max(comwl)
comwl.remove(m4)
m5 = max(comwl)
comwl.remove(m5)

words2 = list(words2)
key1 = keyl[ocomwl.index(m1)]
key2 = keyl[ocomwl.index(m2)]
key3 = keyl[ocomwl.index(m3)]
key4 = keyl[ocomwl.index(m4)]
key5 = keyl[ocomwl.index(m5)]

tup1 = (m1, key1)
tup2 = (m2, key2)
tup3 = (m3, key3)
tup4 = (m4, key4)
tup5 = (m5, key5)

topfive.append(tup1)
topfive.append(tup2)
topfive.append(tup3)
topfive.append(tup4)
topfive.append(tup5)

topfive.sort()
topfive.sort(reverse=True)
print(topfive)
    
    
    
    
    


