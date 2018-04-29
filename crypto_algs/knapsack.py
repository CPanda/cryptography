"""
Contains functions used for the knapsack functionality.

Dylan Hoban
"""
from crypto_algs.rsa import xgcd

def getbinary(list, ezknap, m, winv):
    converted = []
    binaryresult = []
    result = ''
    ezknap.sort(reverse=True)
    for i in list:
        converted.append(i*winv%m)
    for item in converted:
        binaryresult.append(result[::-1])
        result = ''
        for ezitem in ezknap:
            print("EzItem ", ezitem, "ITEM : ", item)
            if(item>=ezitem):
                result+='1'
                item-=ezitem
            else:
                result+='0'
    binaryresult.append(result[::-1])
    return binaryresult




def find_winv(m, w):
    b0,x0,y0 = xgcd(m,w)
    print(b0,x0,y0)
    if (y0<0):
        y0 += m
    return y0 #this is winv

def find_easy_knap(list, m, winv):
    result = []
    for i in list:
        result.append(i*winv%m)
    return result
