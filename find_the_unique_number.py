#https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    i=0
    while(i<len(arr)):
        if(i!=len(arr)-1 and i!=0 and arr[i-1]==arr[i] and arr[i]!=arr[i+1]) :
            return arr[i+1]
        if(i!=len(arr)-1 and arr[i-1]!=arr[i] and arr[i]==arr[i+1]) :
            return arr[i-1]
        i+=1
        
