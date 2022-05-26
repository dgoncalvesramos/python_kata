import math
def binary_array_to_number(arr):
    result=0
    arr = arr[::-1]
    i=0
    while(i<len(arr)):
        result+=arr[i]*math.pow(2,i)
        i+=1
    return result
