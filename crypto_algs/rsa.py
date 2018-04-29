"""
Includes RSA functions

Dylan Hoban
"""

from sympy import factorint
import math

def encrypt(list, n, e):
    result=[]
    print("n : ", n, "e: ", e, "list :", list)
    for i in list:
        result.append(pow(i, e, n))
    return result

def decrypt(list, n, d):
    result = []
    for i in list:
        result.append(pow(i,d,n))
    return result

def find_d(p,q,e):
    b = (p-1)*(q-1)
    b0,x0,y0 = xgcd(b,e)
    if (y0<0):
        y0 += b
    return y0 #this is d.


"""
Returns b, x0, y0 and ax0 + by0 = b
"""

def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

"""
Returns the prime factors of a number
"""

def getpq(n):
    return [*factorint(n)]