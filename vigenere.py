"""
This class handles the Vigenere Cipher.

Needs to be transformed into an object instead of collection of functions. (probably)
"""

import collections
import re
import math
import functools

"""
Temporary testing function. This will be removed later on. 
"""
def main():
    text = input("Enter text\n")
    text = processtext(text) #turn text into all lowercase letters for processing.
    print(friedmantest(text)) #perform friedman test
    print(encrypt(text, 'pie'))
    print(decrypt(text, 'pie'))
    print(kasiskitest(text))



def processtext(text):
    text = text.lower() #transform to lower case
    regex = re.compile('[^a-zA-Z]')
    text = regex.sub('', text) #remove non-letter items.
    regex = re.compile(r'\s+')
    text = regex.sub('', text) #remove all whitespace
    return text


"""
Performs the Friedman test on the entered ciphertext. 

"""
def friedmantest(ciphertext):
    analyze = frequency(ciphertext)
    numberofletters = len(ciphertext)
    total = 0
    for key in analyze:
        total += analyze[key]*(analyze[key]-1) #n(n-1) for each letter found in string
    if((numberofletters-1) != 0): #check for division by zero
        return total/(numberofletters*(numberofletters-1)) #( sum of n(n-1) ) / total # of letters
    else:
        return "not able to calculate"


"""
Decrypts using the Vigenere Cipher
"""

def decrypt(ciphertext, key):
    i = 0
    ordnumber = 0
    j = len(key)
    decrypted = ''
    for c in ciphertext:
        if (i == j):
            i = 0
        ordnumber = ord(c) - (ord(key[i])-97)
        if(ordnumber < 97):
            ordnumber += 26
        decrypted += chr(ordnumber)
        i+=1
    return decrypted

"""
Kasiski test

Still a work in progress. 
"""

def kasiskitest(ciphertext):
    # Goes through the message and finds any 3 to 5 letter sequences
    # that are repeated. Returns a dict with the keys of the sequence and
    # values of a list of spacings (num of letters between the repeats).

    # Compile a list of seqLen-letter sequences found in the message.
    spacings = []
    seqSpacings = {} # keys are sequences, values are list of int spacings
    for seqLen in range(3, 6):
        for seqStart in range(len(ciphertext) - seqLen):
            # Determine what the sequence is, and store it in seq
            seq = ciphertext[seqStart:seqStart + seqLen]

            # Look for this sequence in the rest of the message
            for i in range(seqStart + seqLen, len(ciphertext) - seqLen):
                if ciphertext[i:i + seqLen] == seq:
                    # Found a repeated sequence.
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] # initialize blank list

                    # Append the spacing distance between the repeated
                    # sequence and the original sequence.
                    spacings.append(i-seqStart)
                    seqSpacings[seq].append(i - seqStart)
    if(len(spacings) > 2):
        result = spacings[0]
        for i in spacings[1:]:
            result = math.gcd(result, i)
        return result
    elif(len(spacings) == 2):
        return math.gcd(spacings[0],spacings[1])
    elif(len(spacings) == 0):
        return
    else:
        return spacings[0]




"""
Encrypts using the Vigenere cipher. 

"""

def encrypt(plaintext, key):
    i = 0
    ordnumber = 0
    j = len(key)
    crypted = ''
    for c in plaintext:
        if (i == j):
            i = 0
        ordnumber = ord(c) + (ord(key[i])-97)
        if(ordnumber > 122):
            ordnumber -= 26
        crypted += chr(ordnumber)
        i+=1
    return crypted


def frequency(input):
    letters = collections.Counter(input)
    return letters


main() #temporary for testing.

