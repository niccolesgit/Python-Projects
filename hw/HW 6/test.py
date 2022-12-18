# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:25:26 2021

@author: leen8
"""
#-------------------------repeats for the second file-------------------------------

#finds the average word length
list2 = get_words(file2)
tot2 = 0
for x in list2:
    tot2 += len(x)
avg2 = tot2/len(list2)

#finds the total words and distinct words and calculates the ratio
wlist2 = get_words(file2)
disw2 = set(wlist2)
print((len(wlist2)))
print(len(disw2))
ratio2 = len(disw2)/len(wlist2)

print("\nEvaluating document {}".format(file2))
print("1. Average word length: {:.2f}".format(avg2))
print("2. Ratio of distinct words to total words: {:.3f}".format(ratio2))
print("3. Word sets for document {}:".format(file2))

#finds the max length from of all the words in the list 
maxlen2 = len(wlist2[0])
for x in wlist2:
    if len(x) > maxlen2:
        maxlen2 = len(x)
y = 1
while y <= maxlen2:
    words = set()
    for x in wlist2:
        if len(x) == y:
            words.add(x)
    swords = sorted(set(words))
    awords = ' '.join(swords)
    c = len(swords)
    if c <= 6 and y <10:
        print("   {}:   {}: {}".format(y, c, awords))
    elif c < 10 and y>=10:
        print("  {}:   {}: {}".format(y, c, awords))
    elif c >= 10 and y<10:
        print("   {}:  {}: {} {} {} ... {} {} {}".format(y, c,swords[0],swords[1],swords[2],swords[-3],swords[-2],swords[-1]))
    elif c >= 10 and y>=10:
        print("  {}:  {}: {} {} {} ... {} {} {}".format(y, c,swords[0],swords[1],swords[2],swords[-3],swords[-2],swords[-1]))
    y+=1

tuplist2 = get_pairs(wlist2, sep)
stuplist2 = sorted(tuplist2)
pairlen2 = len(tuplist2) + 1
print("4. Word pairs for document {}".format(file2))
print("  {} distinct pairs".format(pairlen2))

print("  {}".format(' '.join(stuplist2[0])))
print("  {}".format(' '.join(stuplist2[1])))
print("  {}".format(' '.join(stuplist2[2])))
print("  {}".format(' '.join(stuplist2[3])))
print("  {}".format(' '.join(stuplist2[4])))
print("  ...")
print("  {}".format(' '.join(stuplist2[-5])))
print("  {}".format(' '.join(stuplist2[-4])))
print("  {}".format(' '.join(stuplist2[-3])))
print("  {}".format(' '.join(stuplist2[-2])))
print("  {}".format(' '.join(stuplist2[-1])))

allpairs2 = get_all_pairs(wlist2, sep)
alllen2 = len(allpairs2) + 1

dratio2 = pairlen2/alllen2
print("5. Ratio of distinct word pairs to total: {:.3f}".format(dratio2))


if swtuple[0] == '':
    bltuples.append(swtuple)
else:
    tuples.append(swtuple)


z = 1
while z <= maxb:
    words1 = set()
    for x in wlist1:
        if len(x) == y:
            words1.add(x)
    swords1 = sorted(set(words))
    words2 = set()
    for x in wlist2:
        if len(x) == y:
            words2.add(x)
    swords1 = sorted(set(words))
    
