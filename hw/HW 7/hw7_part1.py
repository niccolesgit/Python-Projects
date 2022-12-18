# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:20:25 2021

@author: leen8
"""
#imports string module that can get all lower alphabetical letters in a list
import string

#gets and prints the dictionary file, input file, and keyboard file the user inputted
if __name__ == "__main__":
    dict_file = input('Dictionary file => ')
    print(dict_file)
    input_file = input('Input file => ')
    print(input_file)
    keyb_file = input('Keyboard file => ')
    print(keyb_file)

#creates a dictionary from the dictionary file
dict_d = dict()
with open(dict_file) as df:
    for line in df:
        (key, value) = line.strip("\n").split(",")
        dict_d[key] = value

#takes the inputs from the input file and makes it a list
inf = open(input_file).read()
infl = inf.strip().split("\n")

#creates a dictionary of the keyboard file, taking the first letter as the key
# and the rest of the elements of a list of values
dict_k = dict()
with open(keyb_file) as kf:
    for line in kf:
        kfl = line.split()
        dict_k[kfl[0]] = kfl[1:]

# a function that goes through all the autocorrect functions and appends any valid words it all to a set
def result(word):
    res_words = set()
    #drop: splits the word into a list and removes a letter changes it back into a word and checks if its a valid word one character
    #  removal at a time, if it is valid, it adds it to the set
    wordl = list(word)
    for x in range(len(wordl)):
        wordl = list(word)
        del wordl[x]
        new_word = "".join(wordl).strip()
        if new_word in dict_d.keys():
            res_words.add(new_word)
    #insert: splits the word into a list, gets all lowercase letters from the string module, and takes the 
    #  coordinate of x and inserts the letter at every point in the word list, changest it back to a word, 
    #  checks if it's a valid word and adds it to the set
    wordl = list(word)
    for x in range(len(wordl)+1):
        letterl = list(string.ascii_lowercase)
        for y in letterl:
            wordl = list(word)
            wordl.insert(x, y)
            new_word = "".join(wordl).strip()
            if new_word in dict_d.keys():
                res_words.add(new_word)
    #swap: splits the word into a list and goes through each element of the list, swapping the letters two by two
    # changes it back into a word and checks the word, if it is valid it adds it to the set. 
    wordl = list(word)
    for x in range(len(wordl)-1):
        wordl = list(word)
        wordl[x], wordl[x+1] = wordl[x+1], wordl[x]
        new_word = "".join(wordl).strip()
        if new_word in dict_d.keys():
            res_words.add(new_word)
    #replace: splits the word into a list and gets the values of the keyboard dictionary based on what letter in the 
    # the word list it interates into, it replaces the letter in the word list with all the letters in the keyboard
    # dictionary and changes it back into a word and checks if it is a valid word, if it is it adds it to the set
    wordl = list(word)
    for x in range(0, len(wordl)):
        keyl = dict_k[wordl[x]]
        for y in keyl:
            wordl = list(word)
            wordl[x] = y
            new_word = "".join(wordl).strip()
            if new_word in dict_d.keys():
                res_words.add(new_word)
    # returns all the words found through the autocorrect functions above
    return res_words

# goes through every letter in the input words list and calculates the number of spaces required for each word's output
for x in infl:
    space = 15 - len(x)
    strspace = " "*space
    #if the word is a valid word in the dictionary, prints that it is found
    if x in dict_d.keys():
        print(strspace + "{} -> FOUND".format(x))
    #if there is only one autocorrected word, it prints the word, the number of autocorrected words, and the autocorrected word
    elif len(result(x)) == 1:
        strset = " ".join(result(x))
        print(strspace + "{} -> FOUND  {}:  {}".format(x, len(result(x)), strset))
    #if there are more than one autocorrected word it creates a dictonary to store all of the autocorrected words and their 
    # frequency values, adds them to a dictoinary, sorts the dictionary in decsending order, takes the top 3 words changes them
    # into strings and prints the word, word length (if greater than 10, reduces the space for even spacing), and the words
    elif len(result(x)) > 1:
        newdic = dict()
        newl = []
        for i in result(x):
            freq = dict_d.get(i)
            newdic[i] = freq
        freql = sorted(newdic.items(), key=lambda x: x[1], reverse=True)
        freqd = dict(freql[:3])
        freqdl = list(freqd.keys())
        freqw = " ".join(freqdl)
        if len(result(x)) < 10:
            print(strspace+"{} -> FOUND  {}:  {}".format(x, len(result(x)), freqw))
        else:
            print(strspace+"{} -> FOUND {}:  {}".format(x, len(result(x)), freqw))
    #if there are no autocorrected words nor found in the dictionary, then it prints that the word is not found.
    elif len(result(x)) == 0:
        print(strspace+"{} -> NOT FOUND".format(x))    
  