#Author: Ken Koltermann 2/14/17
import random
import sys
import os
from datetime import datetime

def current_time():
    return datetime.datetime.now()

def get_random(x, y):
    print random.randint(x, y)

#did not feel like doing a redex
def get_zipcode_from_address(string):
    strList = list(string)
    length = len(strList)
    zipcode = []
    counter = 0
    for x in range(0,length):
        if strList[x] == '0':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        elif strList[x] == '1':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break    
        elif strList[x] == '2':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        elif strList[x] == '3':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        elif strList[x] == '4':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        elif strList[x] == '5':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        elif strList[x] == '6':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        elif strList[x] == '7':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        elif strList[x] == '8':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        elif strList[x] == '9':
            counter += 1
            zipcode.append(strList[x])
            if counter == 5:
                break
        else:
            counter = 0
            zipcode = []
    return "".join(zipcode)



    

#any functions to be used across many files
