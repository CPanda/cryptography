"""
Contains functions used for the knapsack functionality.

Dylan Hoban
"""
from crypto_algs.rsa import xgcd

def getEncoded(binlist, ezlist, m, w):
    hardknap = []
    result = []
    sum = 0
    for i in ezlist:
        hardknap.append(i*w%m)
    for item in binlist:
        for i in range(len(item)):
            if item[i] == '1':
                sum += hardknap[i]
        result.append(sum)
        sum = 0
    return result



def getbinary(list, ezknap, m, winv):
    converted = []
    binaryresult = []
    result = ''
    ezknap.sort(reverse=True)
    for i in list:
        converted.append(i*winv%m)
    backup = converted[:]
    for i in range(len(converted)):
        #binaryresult.append(result[::-1])
        result = ''
        for ezitem in ezknap:
            if(converted[i]>=ezitem):
                result+='1'
                converted[i]-=ezitem
            else:
                result+='0'
        #If not zero, then try adding the mod to the number.
        if(converted[i]!=0):
            result = ''
            converted[i] = backup[i] + m
            for ezitem in ezknap:
                if (converted[i] >= ezitem):
                    result += '1'
                    converted[i] -= ezitem
                else:
                    result += '0'
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
