# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 15:36:02 2021

@author: Nicole Lee
"""
'imported function from syllables.py'
from syllables import find_num_syllables

'prompts the user to input a parargraph and splits the paragraph'
line = input("Enter a paragraph => ")
print(line)
split_line = line.split()
split_sent = line.split(".")
asl = len(split_line)/len(split_sent)-1
count_asyl = 0
find_num_syllables(line)/len(split_line)

'determines all the hard words within the paragraph from a list and removes \
    any duplicate words, hyphenated words, and words that end with es and \
        ed.'
hlist = []
hard_list = []
hcount = 0
x = 0
asl =  len(split_line)/(len(split_sent)-1)
while x < len(split_line):
    count_asyl += find_num_syllables(split_line[x])
    if find_num_syllables(split_line[x]) >= 3:
        if not "-" in split_line[x]:
            hcount += 1
            hlist.append(split_line[x])
            if not split_line[x] in hard_list:
                hard_list.append(split_line[x])
    elif find_num_syllables(split_line[x]) == 3:
        if not "s" in split_line[x][-1] and not 'e' in split_line[x][-2]:
            if not "d" in split_line[x][-1] and not 'e' in split_line[x][-2]:
                hcount += 1
                hlist.append(split_line[x])
                if not split_line[x] in hard_list:
                    hard_list.append(split_line[x])
    x+=1
'calculates the phw, asyl, gfri, and fkri'
phw = (hcount/len(split_line))*100
asyl = count_asyl/len(split_line)
gfri = 0.4*(asl + phw)
fkri = 206.835-1.015*asl-86.4*asyl

'prints the hard words and stats calculated'
print("Here are the hard words in this paragraph:")
print(hard_list)
print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(asl, phw, asyl))
print("Readability index (GFRI): {:.2f}".format(gfri))
print("Readability index (FKRI): {:.2f}".format(fkri))




    