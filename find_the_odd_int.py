def find_it(seq):
    nb_odds=0
    for element in seq :
        for element_2 in seq :
            if(element == element_2) :
                nb_odds+=1
        if(nb_odds%2==1):
            return element
        else :
            nb_odds=0
    return None

