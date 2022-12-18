# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:00:28 2021

@author: Nicole Lee
"""
'takes the string from the user'
sent = input("Enter a string to encode ==> ")
print(sent)

'encrypts the word using the .replace function'
def encrypt(word):
    esent = word.replace(' a', '%4%').replace('he', '7!').replace('e', '9(*9(').replace('y', '*%$').replace('u', '@@@').replace('an', '-?').replace('th', '!@+3') .replace('o', '7654').replace('9', '2').replace('ck', '%4')
    return esent
'decrypts the word using the .replace function in reverse'
def decrypt(word):
    dsent = word.replace('%4', 'ck').replace('2', '9').replace('7654', 'o').replace('!@+3', 'th').replace('-?', 'an').replace('@@@', 'u').replace('*%$', 'y').replace('9(*9(', 'e').replace('7!', 'he').replace('%4%', ' a')
    return dsent
'assigns the encrypted word into a variable'
encword = encrypt(sent)

'prints the encrypted word'
print("\nEncrypted as ==> {}".format(encword))

'assingns the decrypted word to a variable'
decword = decrypt(encword)

'finds the length of the encrypted and decrypted word and calculates and prints the difference'
enclen = len(encword)
declen = len(decword)
ldiff = enclen - len(sent)
print("Difference in length ==> {}".format(ldiff))

'prints the deciphered word using the output from the function'
print("Deciphered as ==> {}".format(decword))

'uses a comparison to determine whether or not the string was reversable'
if decword == sent:
    print("Operation is reversible on the string.")
else: 
    print("Operation is not reversible on the string.")
