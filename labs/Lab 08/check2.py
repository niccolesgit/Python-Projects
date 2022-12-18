# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 22:21:06 2021

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
def comm_words(f1, f2):
    com_word = []
    for x in f1:
        if x in f2:
            com_word.append(x)
    scom_word = set(com_word)
    return scom_word
def first_unique(f1, comwords):
    first_unique = []
    for x in f1:
        if x in comwords:
            pass
        else:
            first_unique.append(x)
    s1unique = set(first_unique)
    return s1unique
def second_unique(f2, comwords):
    second_unique = []
    for x in f2:
        if x in comwords:
            pass
        else:
            second_unique.append(x)
    s2unique = set(second_unique)
    return s2unique
ifile1 = input("Enter the first file: ")
ifile2 = input("Enter the second file: ")
print("Comparing clubs {} and {}:".format(ifile1, ifile2))
file1 = ifile1 + ".txt"
file2 = ifile2 + ".txt"
f1 = get_words(file1)
f2 = get_words(file2)
print("\nSame words: {}".format(comm_words(f1,f2)))
comwords = comm_words(f1, f2)
print("\nUnique to {}: {}".format(ifile1, first_unique(f1, comwords)))
print("\nUnique to {}: {}".format(ifile2, second_unique(f2, comwords)))






