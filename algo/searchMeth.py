from .utils import cmp;

def linearSearch(key, arr):
    for index in range(len(arr)):
         if arr[index] == key: 
             return index
    return None

arr = [234,34,34534,6456, 345 ,345, 345,234, 456]
ind = linearSearch(345346, arr)
print(ind)