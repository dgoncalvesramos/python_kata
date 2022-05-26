alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,
                'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def find_key(v): 
    for k, val in alphabet.items(): 
        if v == val: 
            return str(k) 

def find_missing_letter(chars):
    i=0
    while(i<len(chars)-1):
        val_1 = alphabet.get(chars[i].lower())
        val_2 = alphabet.get(chars[i+1].lower())
        if(val_2-val_1 != 1):
            letter = find_key(val_2-1)
            if(chars[i].isupper()):
                return letter.upper()
            else :
                return letter
        i+=1 
