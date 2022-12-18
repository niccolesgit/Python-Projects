# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:29:52 2021

@author: leen8
"""
import string

if __name__ == "__main__":
    dict_file = input('Dictionary file => ')
    print(dict_file)
    input_file = input('Input file => ')
    print(input_file)
    keyb_file = input('Keyboard file => ')
    print(keyb_file)

dict_d = dict()
with open(dict_file) as df:
    for line in df:
        (key, value) = line.strip("\n").split(",")
        dict_d[key] = value
inf = open(input_file).read()
infl = inf.strip().split("\n")

dict_k = dict()

with open(keyb_file) as kf:
    for line in kf:
        kfl = line.split()
        dict_k[kfl[0]] = kfl[1:]

res_words = []
def drop(word):
    wordl = list(word)
    for x in range(len(wordl)):
        wordl = list(word)
        del wordl[x]
        new_word = "".join(wordl).strip()
        if new_word in dict_d.keys():
            res_words.append(new_word)
    return list(set(res_words))
def insert(word):
    wordl = list(word)
    for x in range(len(wordl)+1):
        letterl = list(string.ascii_lowercase)
        for y in letterl:
            wordl = list(word)
            wordl.insert(x, y)
            new_word = "".join(wordl).strip()
            if new_word in dict_d.keys():
                res_words.append(new_word)
    return list(set(res_words))
def swap(word):
    wordl = list(word)
    for x in range(len(wordl)+1):
        wordl = list(word)
        wordl[x], wordl[x+1] = wordl[x+1], wordl[x]
        new_word = "".join(wordl).strip()
        if new_word in dict_d.keys():
            res_words.append(new_word)
    return list(set(res_words))
def replace(word):
    wordl = list(word)
    for x in range(0, len(wordl)):
        keyl = dict_k[wordl[x]]
        for y in keyl:
            wordl = list(word)
            wordl[x] = y
            new_word = "".join(wordl).strip()
            if new_word in dict_d.keys():
                res_words.append(new_word)
    return list(set(res_words))
print(replace("figging"))
