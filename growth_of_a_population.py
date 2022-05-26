def nb_year(p0, percent, aug, p):
    nb_years = 0
    while(p0<p) :
        p0 += int(p0*(percent/100)) + aug
        nb_years+=1
    return nb_years
