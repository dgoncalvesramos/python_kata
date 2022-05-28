#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):
    list = []
    for element in l :
        if(isinstance(element,int)) :
            list.append(element)
    return list
