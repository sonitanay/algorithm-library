
from random import randint
from time import strftime
from datetime import datetime as dt
import itertools


def compare(a, b, sign):
    """ compare function that returns :
        1 if a is greater
        -1 if b is greater 
        0 if both are equal
    also takes into account
    infinity symbol '#' which can be positive or negative infinity
    based on sign:
        True for positive infinity and False for negative"""
    if a == '#' or b == '#':
        if a == b : return 0
        if sign:
            return 1 if a == '#' else -1
        else:
            return -1 if a == '#' else 1
    elif a == b:
        return 0
    else:
        return 1 if a > b else -1


def randomArrGenInt(length = 1000, range = 100000):
    
    """ function for generating basic random arrays
    so that i dont have to manually type and check """
    
    arr = []
    i = 0
    while i < length:
        arr.append(randint(0, range))
        i += 1
    
    return arr

def checkSort(arr, asc = True):
    
    """ function for checking the sorting of elements """

    for i in range(1, len(arr)):
        res = compare(arr[i], arr[i - 1], asc)
        if (res == 1 or res == 0) and asc:
            continue
        elif (res == -1 or res == 0) and not asc:
            continue
        else:
            return False
    return True


def currTime():
    """ returns system time in seconds """
    t = dt.now().strftime("%H:%M:%S:%f").split(":")
    total = int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])
    total = total * 1000 + int(t[3]) // 1000

    return total