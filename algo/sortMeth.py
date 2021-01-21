from .utils import *
from math import floor, ceil

def insertionSort(arr, asc = True):   
    for index in range(1,len(arr)):
        key = arr[index]
        i = index - 1
        while i >= 0 and ((asc and arr[i] > key) or (not asc and arr[i] < key)):
                arr[i+1] = arr[i]
                i = i-1
        arr[i+1] = key
    return arr


def mergeSort(arr, asc = True):
    """ base condition: if arr length is less than 2 we return the arr 
    with infinity as the end character """
    length = len(arr)
    if  length < 2:
        arr.append('#')
        return arr
    """ recursion section: split into left arr and right arr 
    where left length = right length + 1 """
    half = ceil(length/2)
    left_arr = [arr[i] for i in range(half)]
    right_arr = [arr[i] for i in range(half, length)]
    left_arr = mergeSort(left_arr, asc)
    right_arr = mergeSort(right_arr, asc)
    """ merge section: comparing left and right arr and combining 
    ignoring the infinities and appending new infinity at the end """
    arr = []
    l = 0
    r = 0
    while l < (len(left_arr)) and r < (len(right_arr)):
        res = compare(left_arr[l], right_arr[r], asc)
        if (not asc and (res == 1 or res == 0)) or (asc and (res == -1 or res == 0)):
            if left_arr[l] != '#':
                arr.append(left_arr[l])
            l += 1
        else:
            if right_arr[r] != '#':
                arr.append(right_arr[r])
            r += 1
    arr.append('#')
    """ final arr returns with an extra '#' at the end 
    that should be removed in post processing for original arr """
    return arr


def mergeSortNoSen(arr, asc = True):
    
    #base condition but no sentinel

    length = len(arr)
    if length < 2:
        return arr

    """ recursion section : same as mergeSort with sentinel """

    half = ceil(length/2)
    left_arr = arr[:half]
    right_arr = arr[half:]
    left_arr = mergeSortNoSen(left_arr, asc)
    right_arr = mergeSortNoSen(right_arr, asc)

    l, r = 0,0
    arr = []

    """ merge section : the while loop continues till either left or right list is completely inserted into the arr
    after this, we know that the remaining elements in the other array are already sorted so we simply insert those
    elements into arr """

    while l < len(left_arr) and r < len(right_arr):
        res = compare(left_arr[l], right_arr[r], asc)
        if (res == -1 and asc) or (res == 1 and not asc):
            arr.append(left_arr[l])
            l += 1
        else:
            arr.append(right_arr[r])
            r += 1
    
    if l == len(left_arr):
        for j in range(r, len(right_arr)):
            arr.append(right_arr[j])
    else:
        for i in range(l, len(left_arr)):
            arr.append(left_arr[i])

    return arr



arr = randomArrGenInt(1000000, 100000)
print(arr,"\n\n")
t1 = currTime()
arr = mergeSortNoSen(arr)
#arr.pop()
t2 = currTime()
print(arr,"\n\n")
print("properly sorted :",checkSort(arr),"\ntime taken :",(t2 - t1), "ms")