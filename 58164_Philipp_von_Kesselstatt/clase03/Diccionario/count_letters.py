def count_letters(s):
    
    d={}
    
    for letter in s:
        if letter in d:
            d[letter]+=1
        else:
            d[letter]=1
         

    return d