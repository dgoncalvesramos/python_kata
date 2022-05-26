def filter_list(l):
    list = []
    for element in l :
        if(isinstance(element,int)) :
            list.append(element)
    return list
