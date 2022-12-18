# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:48:05 2021

@author: Nicole Lee
"""
'imports hw4 utility and re for string comparison'
import hw4_util
import re

'takes the input from the user'
password = input("Enter a password => ")
print(password)
'checks the length, striping any additional spaces before checking the length and calulates and prints the score'
def length(password):
    lscore = 0
    spass = password.strip()
    lpass = len(spass)
    if lpass == 6 or lpass == 7:
        lscore +=1
    elif lpass > 7 and lpass <= 10:
        lscore +=2
    elif lpass > 10:
        lscore +=3
    else:
        lscore += 0
    if lscore > 0:
        print("Length: +{}".format(lscore))
    return lscore
'determines the number of upper and lowercase letters in the password and calculates and prints the score'
def case(password):
    l = 0
    u = 0
    cscore = 0
    for x in password:
        if x.isupper():
           u+=1
        elif x.islower():
            l +=1
    if u >= 2 and l >= 2:
       cscore+=2
    elif u >= 1 and l >= 1:
       cscore +=1
    if cscore > 0:
        print("Cases: +{}".format(cscore))
    return cscore
'finds the number of numbers and calculates and prints the score'
def digits(password):
    n = 0
    dscore = 0
    for x in password:
        if x.isdigit():
            n += 1
    if n >= 2:
       dscore+=2
    elif n == 1:
       dscore +=1
    if dscore > 0:
        print("Digits: +{}".format(dscore))
    return dscore
'determines if there are special characters and calculates and prints the score based on the group of special characters its in'
def chars(password):
    p1 = 0
    p2 = 0
    p1score = 0
    p2score = 0
    ec = password.count('!')
    ac = password.count('@')
    hc = password.count('#')
    mc = password.count('$')
    tcount1 = ec+ac+hc+mc
    if tcount1 > 0:
        p1+=1
    pc = password.count('%')
    exc = password.count('^')
    anc = password.count('&')
    sc = password.count('*')
    tcount2 = pc+exc+anc+sc
    if tcount2 > 0:
        p2+=1
    if p1 >= 1:
        p1score+=1
    elif p2 >= 1:
        p2score +=1
    if p1score > 0:
        print("!@#$: +{}".format(p1score))
    if p2score > 0:
        print("%^&*: +{}".format(p2score))
    return p1score + p2score
'uses re to compare the license plate pattern and takes it in any case and removes the spaces and calculates and prints the score'
def ny_licen(password):
    lpass = password.strip().lower()
    nyscore = 0
    nylicen = re.compile("[a-z][a-z][a-z][0-9][0-9][0-9][0-9]+$")
    verif = bool(nylicen.match(lpass))
    if verif == True:
        nyscore -=2
        print("License: {}".format(nyscore))
    else:
        nyscore += 0
    return nyscore
'takes the password and dertmines if the password is in the list of common passwords calculating the score and printa the score '
def common(password):
    lpass = password.strip().lower()
    comscore = 0
    lcomm = hw4_util.part1_get_top()
    lcomm = list(lcomm)
    if lcomm.count(lpass) > 0:
            comscore -=3
    if comscore < 0:
        print("Common: {}".format(comscore))
    return comscore
'calculates the and prints the combined score'
comb_score = length(password) + case(password) + digits(password) + chars(password) + ny_licen(password) + common(password)
print("Combined score: {}".format(comb_score))
'takes the combined score and determines the grade of the password and prints it'
if comb_score <= 0:
    grade = "rejected"
elif comb_score <= 2:
    grade = "poor"
elif comb_score <=4:
    grade = "fair"
elif comb_score <= 6:
    grade = "good"
elif comb_score >= 7:
    grade = "excellent"
print("Password is {}".format(grade))

