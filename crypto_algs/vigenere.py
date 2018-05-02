"""
These functions handle the Vigenere Cipher.

Dylan Hoban

"""

import collections
import re
import math
import functools

"""
Temporary testing function. This will be removed later on.
"""



def main1():
    text = input("Enter text\n")
    text = processtext(text)  # turn text into all lowercase letters for processing.
    print(friedmantest(text))  # perform friedman test
    print(encrypt(text, 'pie'))
    print(decrypt(text, 'pie'))
    print(kasiskitest(text))


def processtext(text):
    text = text.lower()  # transform to lower case
    regex = re.compile('[^a-zA-Z]')
    text = regex.sub('', text)  # remove non-letter items.
    regex = re.compile(r'\s+')
    text = regex.sub('', text)  # remove all whitespace
    return text


"""
Performs the Friedman test on the entered ciphertext. 

"""


def friedmantest(ciphertext):
    analyze = frequency(ciphertext)
    numberofletters = len(ciphertext)
    total = 0
    for key in analyze:
        total += analyze[key] * (analyze[key] - 1)  # n(n-1) for each letter found in string
    if ((numberofletters - 1) != 0):  # check for division by zero
        return total / (numberofletters * (numberofletters - 1))  # ( sum of n(n-1) ) / total # of letters
    else:
        return "not able to calculate"


"""
Decrypts using the Vigenere Cipher
"""


def decrypt(ciphertext, key):
    ciphertext = processtext(ciphertext)
    i = 0
    ordnumber = 0
    j = len(key)
    decrypted = ''
    for c in ciphertext:
        if (i == j):
            i = 0
        ordnumber = ord(c) - (ord(key[i]) - 97)
        if (ordnumber < 97):
            ordnumber += 26
        decrypted += chr(ordnumber)
        i += 1
    return decrypted




"""
Encrypts using the Vigenere cipher. 

"""


def encrypt(plaintext, key):
    plaintext = processtext(plaintext)
    i = 0
    ordnumber = 0
    j = len(key)
    crypted = ''
    for c in plaintext:
        if (i == j):
            i = 0
        ordnumber = ord(c) + (ord(key[i]) - 97)
        if (ordnumber > 122):
            ordnumber -= 26
        crypted += chr(ordnumber)
        i += 1
    return crypted


def frequency(input):
    letters = collections.Counter(input)
    return letters

# main() #temporary for testing.
