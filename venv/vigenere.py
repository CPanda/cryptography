"""
This class handles the Vigenere Cipher.
"""

import collections
import re



def main():
    text = input("Enter text\n")
    text = processtext(text) #turn text into all lowercase letters for processing.
    print(ord('a'))
    print(friedmantest(text)) #perform friedman test
    print(encrypt(text, 'pie'))
    print(decrypt(text, 'pie'))



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
    return total/numberofletters #( sum of n(n-1) ) / total # of letters


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

