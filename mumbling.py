def accum(s):
    i=0
    str_res=""
    while(i<len(s)):
        t=0
        while(t<=i):
            if(t==0):
                str_res+=s[i].upper()
            else :
                str_res+=s[i].lower()
            t+=1
        if(i!=len(s)-1) :
            str_res+="-"
        t=0 
        i+=1
    return str_res
