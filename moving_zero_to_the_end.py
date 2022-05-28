#https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    nb_zeros=0
    res=[]
    for element in array :
        if(element!=0):
            res.append(element)
        if(element==0):
            nb_zeros+=1
    while(nb_zeros!=0):
        res.append(0)
        nb_zeros-=1
    return res
             
