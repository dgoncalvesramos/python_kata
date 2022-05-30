#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/

def max_sequence(arr):
    
    if (len(arr)==0):
        return 0
    
    max_so_far =arr[0]
    curr_max = arr[0]
    for i in range(1,len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far,curr_max)
    if(max_so_far<0) :
        return 0
    return max_so_far
                   
          
